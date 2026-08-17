const vscode = require('vscode');
const { spawn } = require('child_process');

let terminal;
let diagnostics;
let hintDecoration;
let statusBar;
let wordEntries = [];
let wordMap = new Map();
let lastCoreRefresh = 0;
let refreshPromise;
const diagnosticTimers = new Map();

function configuredExecutable() {
  return vscode.workspace.getConfiguration('kopy').get('executablePath', 'kopy').trim() || 'kopy';
}

function invokeJson(args, input = '') {
  return new Promise((resolve, reject) => {
    const child = spawn(configuredExecutable(), args, {
      windowsHide: true,
      shell: false,
    });

    let stdout = '';
    let stderr = '';
    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');
    child.stdout.on('data', chunk => { stdout += chunk; });
    child.stderr.on('data', chunk => { stderr += chunk; });
    child.on('error', reject);
    child.on('close', () => {
      try {
        resolve(JSON.parse(stdout.trim()));
      } catch (error) {
        reject(new Error(stderr.trim() || stdout.trim() || error.message));
      }
    });

    if (input) child.stdin.write(input, 'utf8');
    child.stdin.end();
  });
}

async function refreshCoreData(force = false) {
  const now = Date.now();
  if (!force && wordEntries.length && now - lastCoreRefresh < 2000) return;
  if (refreshPromise) return refreshPromise;

  refreshPromise = (async () => {
    const [words, info] = await Promise.all([
      invokeJson(['words', '--json']),
      invokeJson(['info', '--json']),
    ]);

    wordEntries = Array.isArray(words.words) ? words.words : [];
    wordMap = new Map(wordEntries.map(entry => [entry.kopy, entry]));
    lastCoreRefresh = Date.now();

    statusBar.text = `KoPy ${info.kopy_version}`;
    statusBar.tooltip = `KoPy ${info.kopy_version} · 기준 Python ${info.python_baseline} · 실행 Python ${info.runtime_python}`;
  })().finally(() => {
    refreshPromise = undefined;
  });

  return refreshPromise;
}

function quoteCmd(value) {
  return `"${String(value).replace(/"/g, '""')}"`;
}

async function runCurrentFile() {
  const editor = vscode.window.activeTextEditor;
  if (!editor || editor.document.languageId !== 'kopy') {
    vscode.window.showWarningMessage('KoPy: 실행할 .kpy 파일을 먼저 여세요.');
    return;
  }

  const document = editor.document;
  if (document.isDirty && !(await document.save())) {
    vscode.window.showErrorMessage('KoPy: 파일을 저장하지 못해 실행을 중단했습니다.');
    return;
  }

  if (!terminal) {
    if (process.platform === 'win32' && process.env.ComSpec) {
      terminal = vscode.window.createTerminal({ name: 'KoPy', shellPath: process.env.ComSpec });
    } else {
      terminal = vscode.window.createTerminal({ name: 'KoPy' });
    }
  }

  terminal.show(true);
  const executable = configuredExecutable();
  const file = document.uri.fsPath;
  if (process.platform === 'win32') {
    terminal.sendText(`chcp 65001>nul && ${quoteCmd(executable)} ${quoteCmd(file)}`);
  } else {
    terminal.sendText(`${quoteCmd(executable)} ${quoteCmd(file)}`);
  }
}

function completionKind(category) {
  if (category === 'keyword') return vscode.CompletionItemKind.Keyword;
  if (category === 'constant') return vscode.CompletionItemKind.Constant;
  if (category === 'builtin') return vscode.CompletionItemKind.Function;
  return vscode.CompletionItemKind.Text;
}

async function completionItems() {
  await refreshCoreData();
  return wordEntries.map(entry => {
    const item = new vscode.CompletionItem(entry.kopy, completionKind(entry.category));
    item.detail = `Python: ${entry.python}`;
    item.documentation = new vscode.MarkdownString(
      `KoPy **${entry.kopy}** → Python \`${entry.python}\`\n\n분류: ${entry.category}`
    );
    item.insertText = entry.kopy;
    return item;
  });
}

function diagnosticRange(document, item) {
  const startLine = Math.max(0, (item.line || 1) - 1);
  const startColumn = Math.max(0, (item.column || 1) - 1);
  const endLine = Math.max(startLine, (item.end_line || item.line || 1) - 1);
  const endColumn = Math.max(
    startColumn + 1,
    (item.end_column || ((item.column || 1) + 1)) - 1
  );

  const safeStartLine = Math.min(startLine, Math.max(0, document.lineCount - 1));
  const safeEndLine = Math.min(endLine, Math.max(0, document.lineCount - 1));
  const start = new vscode.Position(
    safeStartLine,
    Math.min(startColumn, document.lineAt(safeStartLine).text.length)
  );
  const end = new vscode.Position(
    safeEndLine,
    Math.min(endColumn, document.lineAt(safeEndLine).text.length)
  );
  return new vscode.Range(start, end.isAfter(start) ? end : start.translate(0, 1));
}

async function diagnoseDocument(document) {
  if (!document || document.languageId !== 'kopy') return;

  const spellingEnabled = vscode.workspace.getConfiguration('kopy').get('spelling.enabled', true);
  const version = document.version;

  try {
    const payload = await invokeJson(
      ['diagnose', document.uri.fsPath, '--stdin', '--json'],
      document.getText()
    );

    if (document.isClosed || document.version !== version) return;

    const items = Array.isArray(payload.diagnostics) ? payload.diagnostics : [];
    const visibleItems = spellingEnabled ? items : items.filter(item => item.code !== 'spelling');

    diagnostics.set(document.uri, visibleItems.map(item => {
      const severity = item.severity === 'error'
        ? vscode.DiagnosticSeverity.Error
        : vscode.DiagnosticSeverity.Warning;
      const d = new vscode.Diagnostic(diagnosticRange(document, item), `KoPy: ${item.message}`, severity);
      d.source = 'KoPy Core';
      d.code = item.code;
      return d;
    }));

    const editor = vscode.window.activeTextEditor;
    if (editor?.document.uri.toString() === document.uri.toString()) {
      const spellingItems = visibleItems.filter(item => item.code === 'spelling' && item.suggestion);
      editor.setDecorations(hintDecoration, spellingItems.map(item => ({
        range: diagnosticRange(document, item),
        renderOptions: { after: { contentText: `  # → ${item.suggestion}?` } },
      })));
    }
  } catch (error) {
    diagnostics.delete(document.uri);
    const editor = vscode.window.activeTextEditor;
    if (editor?.document.uri.toString() === document.uri.toString()) {
      editor.setDecorations(hintDecoration, []);
    }
    statusBar.text = 'KoPy 연결 오류';
    statusBar.tooltip = `KoPy 명령을 실행할 수 없습니다: ${error.message}`;
  }
}

function scheduleDiagnosis(document, delay = 180) {
  if (!document || document.languageId !== 'kopy') return;
  const key = document.uri.toString();
  const previous = diagnosticTimers.get(key);
  if (previous) clearTimeout(previous);
  const timer = setTimeout(() => {
    diagnosticTimers.delete(key);
    diagnoseDocument(document);
  }, delay);
  diagnosticTimers.set(key, timer);
}

async function refreshAll(force = true) {
  try {
    await refreshCoreData(force);
  } catch (error) {
    statusBar.text = 'KoPy 연결 오류';
    statusBar.tooltip = `PATH에서 KoPy를 찾을 수 없거나 Core API를 호출하지 못했습니다: ${error.message}`;
    vscode.window.showWarningMessage(
      "KoPy VS Code: 'kopy' 명령에 연결하지 못했습니다. 터미널에서 'kopy version'을 확인하세요."
    );
  }
  vscode.workspace.textDocuments.forEach(document => scheduleDiagnosis(document, 0));
}

function activate(context) {
  diagnostics = vscode.languages.createDiagnosticCollection('kopy');
  hintDecoration = vscode.window.createTextEditorDecorationType({
    after: { color: new vscode.ThemeColor('editorCodeLens.foreground'), fontStyle: 'italic' },
  });
  statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 90);
  statusBar.text = 'KoPy 연결 중…';
  statusBar.tooltip = "PATH의 'kopy' 명령에 연결합니다.";

  context.subscriptions.push(diagnostics, hintDecoration, statusBar);
  context.subscriptions.push(vscode.commands.registerCommand('kopy.runFile', runCurrentFile));
  context.subscriptions.push(vscode.commands.registerCommand('kopy.refreshCore', () => refreshAll(true)));
  context.subscriptions.push(vscode.commands.registerCommand('kopy.toggleSpelling', async () => {
    const cfg = vscode.workspace.getConfiguration('kopy');
    const current = cfg.get('spelling.enabled', true);
    await cfg.update('spelling.enabled', !current, vscode.ConfigurationTarget.Global);
    vscode.window.showInformationMessage(`KoPy 스펠링 힌트: ${!current ? 'ON' : 'OFF'}`);
    vscode.workspace.textDocuments.forEach(document => scheduleDiagnosis(document, 0));
  }));

  context.subscriptions.push(vscode.languages.registerCompletionItemProvider(
    { language: 'kopy', scheme: 'file' },
    { provideCompletionItems: () => completionItems() }
  ));

  context.subscriptions.push(vscode.languages.registerHoverProvider(
    { language: 'kopy', scheme: 'file' },
    {
      async provideHover(document, position) {
        if (!vscode.workspace.getConfiguration('kopy').get('inlinePythonHints', true)) return undefined;
        await refreshCoreData();
        const range = document.getWordRangeAtPosition(position, /[가-힣A-Za-z_][가-힣A-Za-z0-9_]*/);
        if (!range) return undefined;
        const word = document.getText(range);
        const entry = wordMap.get(word);
        if (!entry) return undefined;
        return new vscode.Hover(
          new vscode.MarkdownString(`**KoPy** \`${entry.kopy}\` → **Python** \`${entry.python}\``),
          range
        );
      },
    }
  ));

  context.subscriptions.push(vscode.workspace.onDidOpenTextDocument(document => scheduleDiagnosis(document, 0)));
  context.subscriptions.push(vscode.workspace.onDidChangeTextDocument(event => scheduleDiagnosis(event.document)));
  context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor(editor => {
    if (editor?.document.languageId === 'kopy') {
      statusBar.show();
      refreshCoreData().catch(() => {});
      scheduleDiagnosis(editor.document, 0);
    } else {
      statusBar.hide();
    }
  }));
  context.subscriptions.push(vscode.window.onDidChangeWindowState(state => {
    if (state.focused) refreshCoreData(true).catch(() => {});
  }));
  context.subscriptions.push(vscode.workspace.onDidChangeConfiguration(event => {
    if (event.affectsConfiguration('kopy')) refreshAll(true);
  }));
  context.subscriptions.push(vscode.window.onDidCloseTerminal(t => {
    if (t === terminal) terminal = undefined;
  }));

  refreshAll(true);
  if (vscode.window.activeTextEditor?.document.languageId === 'kopy') statusBar.show();
}

function deactivate() {
  for (const timer of diagnosticTimers.values()) clearTimeout(timer);
  diagnosticTimers.clear();
  terminal = undefined;
}

module.exports = { activate, deactivate };

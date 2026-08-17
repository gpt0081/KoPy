const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

const KO_TO_PY = {
  '펄스': 'False', '논': 'None', '트루': 'True',
  '앤드': 'and', '애즈': 'as', '어설트': 'assert', '어싱크': 'async', '어웨이트': 'await',
  '브레이크': 'break', '클래스': 'class', '컨티뉴': 'continue', '데프': 'def', '델': 'del',
  '엘리프': 'elif', '엘스': 'else', '익셉트': 'except', '파이널리': 'finally', '포': 'for',
  '프롬': 'from', '글로벌': 'global', '이프': 'if', '임포트': 'import', '인': 'in',
  '이즈': 'is', '람다': 'lambda', '논로컬': 'nonlocal', '낫': 'not', '오어': 'or',
  '패스': 'pass', '레이즈': 'raise', '리턴': 'return', '트라이': 'try', '와일': 'while',
  '위드': 'with', '일드': 'yield',
  '프린트': 'print', '인풋': 'input', '인트': 'int', '플로트': 'float', '스트링': 'str',
  '불': 'bool', '바이트': 'bytes', '리스트': 'list', '딕트': 'dict', '튜플': 'tuple',
  '셋': 'set', '렌': 'len', '레인지': 'range', '오픈': 'open', '타입': 'type',
  '썸': 'sum', '민': 'min', '맥스': 'max', '앱스': 'abs', '라운드': 'round',
  '소티드': 'sorted', '이뉴머레이트': 'enumerate', '집': 'zip', '맵': 'map', '필터': 'filter',
  '올': 'all', '애니': 'any', '아이디': 'id', '헬프': 'help', '디르': 'dir',
  '리버스드': 'reversed', '슬라이스': 'slice', '슈퍼': 'super', '오브젝트': 'object',
  '아이시인스턴스': 'isinstance', '아이서브클래스': 'issubclass', '콜러블': 'callable',
  '크르': 'chr', '오드': 'ord', '빈': 'bin', '옥트': 'oct', '헥스': 'hex', '파우': 'pow'
};

const PY_KEYWORDS = new Set([
  'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
  'try', 'while', 'with', 'yield', 'match', 'case'
]);

const PY_BUILTINS = new Set([
  'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray',
  'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir',
  'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'getattr',
  'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
  'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
  'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set',
  'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'
]);

let terminal;
let diagnostics;
let hintDecoration;
let statusBar;

function oneEditOrSwap(a, b) {
  if (a === b || Math.abs(a.length - b.length) > 1) return false;
  if (a.length === b.length) {
    const diffs = [];
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) diffs.push(i);
    if (diffs.length === 1) return true;
    if (diffs.length === 2) {
      const [i, j] = diffs;
      return j === i + 1 && a[i] === b[j] && a[j] === b[i];
    }
    return false;
  }
  const short = a.length < b.length ? a : b;
  const long = a.length < b.length ? b : a;
  let i = 0, j = 0, misses = 0;
  while (i < short.length && j < long.length) {
    if (short[i] === long[j]) { i++; j++; continue; }
    misses++;
    if (misses > 1) return false;
    j++;
  }
  return true;
}

function bestCandidate(word, candidates) {
  const hits = [...candidates].filter(x => oneEditOrSwap(word, x));
  if (!hits.length) return undefined;
  hits.sort((a, b) => Math.abs(a.length - word.length) - Math.abs(b.length - word.length));
  return hits[0];
}

function scanIdentifiers(text) {
  const out = [];
  let i = 0, line = 0, col = 0;
  let state = 'normal';
  let quote = '';

  const advance = (ch) => {
    if (ch === '\n') { line++; col = 0; } else col++;
    i++;
  };

  while (i < text.length) {
    const ch = text[i];

    if (state === 'comment') {
      advance(ch);
      if (ch === '\n') state = 'normal';
      continue;
    }

    if (state === 'string') {
      if (ch === '\\') {
        advance(ch);
        if (i < text.length) advance(text[i]);
        continue;
      }
      if (text.startsWith(quote, i)) {
        for (let k = 0; k < quote.length; k++) advance(text[i]);
        state = 'normal';
        continue;
      }
      advance(ch);
      continue;
    }

    if (ch === '#') { state = 'comment'; advance(ch); continue; }
    if (text.startsWith("'''", i) || text.startsWith('\"\"\"', i)) {
      quote = text.substr(i, 3); state = 'string';
      for (let k = 0; k < 3; k++) advance(text[i]);
      continue;
    }
    if (ch === "'" || ch === '\"') {
      quote = ch; state = 'string'; advance(ch); continue;
    }

    if (/[A-Za-z_]/.test(ch)) {
      const start = i, startLine = line, startCol = col;
      while (i < text.length && /[A-Za-z0-9_]/.test(text[i])) advance(text[i]);
      out.push({ word: text.slice(start, i), start, end: i, line: startLine, col: startCol });
      continue;
    }

    advance(ch);
  }
  return out;
}

function findHints(document) {
  const text = document.getText();
  const hints = [];
  for (const token of scanIdentifiers(text)) {
    const word = token.word;
    if (PY_KEYWORDS.has(word) || PY_BUILTINS.has(word)) continue;

    let p = token.start - 1;
    while (p >= 0 && /\s/.test(text[p])) p--;
    if (p >= 0 && text[p] === '.') continue;

    let suggestion = bestCandidate(word, PY_KEYWORDS);
    if (!suggestion) {
      let n = token.end;
      while (n < text.length && /\s/.test(text[n])) n++;
      if (text[n] === '(') suggestion = bestCandidate(word, PY_BUILTINS);
    }
    if (!suggestion) continue;

    const range = new vscode.Range(
      new vscode.Position(token.line, token.col),
      new vscode.Position(token.line, token.col + word.length)
    );
    hints.push({ word, suggestion, range });
  }
  return hints;
}

function refreshDocument(document) {
  if (!document || document.languageId !== 'kopy') return;
  const enabled = vscode.workspace.getConfiguration('kopy').get('spelling.enabled', true);
  if (!enabled) {
    diagnostics.delete(document.uri);
    if (vscode.window.activeTextEditor?.document.uri.toString() === document.uri.toString()) {
      vscode.window.activeTextEditor.setDecorations(hintDecoration, []);
    }
    return;
  }

  const hints = findHints(document);
  diagnostics.set(document.uri, hints.map(h => {
    const d = new vscode.Diagnostic(
      h.range,
      `KoPy: '${h.word}' → '${h.suggestion}' 를 입력하려고 했나요?`,
      vscode.DiagnosticSeverity.Warning
    );
    d.source = 'KoPy';
    d.code = 'spelling';
    return d;
  }));

  const editor = vscode.window.activeTextEditor;
  if (editor?.document.uri.toString() === document.uri.toString()) {
    editor.setDecorations(hintDecoration, hints.map(h => ({
      range: h.range,
      renderOptions: { after: { contentText: `  # → ${h.suggestion}?` } }
    })));
  }
}

function quoteCmd(value) {
  return `\"${String(value).replace(/\"/g, '\"\"')}\"`;
}

function resolveExecutable(document) {
  const configured = vscode.workspace.getConfiguration('kopy').get('executablePath', '').trim();
  if (configured) return configured;
  const folder = vscode.workspace.getWorkspaceFolder(document.uri);
  if (folder && process.platform === 'win32') {
    const localExe = path.join(folder.uri.fsPath, 'dist', 'kopy.exe');
    if (fs.existsSync(localExe)) return localExe;
  }
  return 'kopy';
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

  const executable = resolveExecutable(document);
  const file = document.uri.fsPath;

  if (!terminal) {
    if (process.platform === 'win32' && process.env.ComSpec) {
      terminal = vscode.window.createTerminal({ name: 'KoPy', shellPath: process.env.ComSpec });
    } else {
      terminal = vscode.window.createTerminal({ name: 'KoPy' });
    }
  }
  terminal.show(true);

  if (process.platform === 'win32') {
    terminal.sendText(`chcp 65001>nul && ${quoteCmd(executable)} ${quoteCmd(file)}`);
  } else {
    terminal.sendText(`${quoteCmd(executable)} ${quoteCmd(file)}`);
  }
}

function makeCompletionItems() {
  return Object.entries(KO_TO_PY).map(([ko, py]) => {
    const item = new vscode.CompletionItem(ko, vscode.CompletionItemKind.Keyword);
    item.detail = `Python: ${py}`;
    item.documentation = new vscode.MarkdownString(`KoPy **${ko}** → Python \`${py}\``);
    item.insertText = ko;
    return item;
  });
}

function activate(context) {
  diagnostics = vscode.languages.createDiagnosticCollection('kopy');
  hintDecoration = vscode.window.createTextEditorDecorationType({
    after: { color: new vscode.ThemeColor('editorCodeLens.foreground'), fontStyle: 'italic' }
  });
  statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 90);
  statusBar.text = 'KoPy 3.12.10';
  statusBar.tooltip = 'KoPy 기준 Python 3.12.10';

  context.subscriptions.push(diagnostics, hintDecoration, statusBar);
  context.subscriptions.push(vscode.commands.registerCommand('kopy.runFile', runCurrentFile));
  context.subscriptions.push(vscode.commands.registerCommand('kopy.toggleSpelling', async () => {
    const cfg = vscode.workspace.getConfiguration('kopy');
    const current = cfg.get('spelling.enabled', true);
    await cfg.update('spelling.enabled', !current, vscode.ConfigurationTarget.Global);
    vscode.window.showInformationMessage(`KoPy 스펠링 힌트: ${!current ? 'ON' : 'OFF'}`);
  }));

  context.subscriptions.push(vscode.languages.registerCompletionItemProvider(
    { language: 'kopy', scheme: 'file' },
    { provideCompletionItems: () => makeCompletionItems() }
  ));

  context.subscriptions.push(vscode.languages.registerHoverProvider(
    { language: 'kopy', scheme: 'file' },
    {
      provideHover(document, position) {
        if (!vscode.workspace.getConfiguration('kopy').get('inlinePythonHints', true)) return undefined;
        const range = document.getWordRangeAtPosition(position, /[가-힣A-Za-z_][가-힣A-Za-z0-9_]*/);
        if (!range) return undefined;
        const word = document.getText(range);
        const py = KO_TO_PY[word];
        if (!py) return undefined;
        return new vscode.Hover(new vscode.MarkdownString(`**KoPy** \`${word}\` → **Python** \`${py}\``), range);
      }
    }
  ));

  context.subscriptions.push(vscode.workspace.onDidOpenTextDocument(refreshDocument));
  context.subscriptions.push(vscode.workspace.onDidChangeTextDocument(e => refreshDocument(e.document)));
  context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor(editor => {
    if (editor?.document.languageId === 'kopy') {
      statusBar.show();
      refreshDocument(editor.document);
    } else {
      statusBar.hide();
    }
  }));
  context.subscriptions.push(vscode.workspace.onDidChangeConfiguration(e => {
    if (e.affectsConfiguration('kopy')) {
      vscode.workspace.textDocuments.forEach(refreshDocument);
    }
  }));
  context.subscriptions.push(vscode.window.onDidCloseTerminal(t => {
    if (t === terminal) terminal = undefined;
  }));

  vscode.workspace.textDocuments.forEach(refreshDocument);
  if (vscode.window.activeTextEditor?.document.languageId === 'kopy') statusBar.show();
}

function deactivate() {
  terminal = undefined;
}

module.exports = { activate, deactivate };

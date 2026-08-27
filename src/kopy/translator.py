"""Token-safe translation between KoPy and Python."""

from __future__ import annotations

import ast
import io
import tokenize
from dataclasses import dataclass

from .packs.registry import all_packs
from .words import COMMON_IDENTIFIERS, COMMON_PY_TO_KO, PY_TO_KO, WORDS


@dataclass(frozen=True)
class Translation:
    source: str
    python: str
    replacements: tuple[tuple[str, str, int, int], ...]


@dataclass(frozen=True)
class ReverseTranslation:
    source: str
    kopy: str
    replacements: tuple[tuple[str, str, int, int], ...]


@dataclass(frozen=True)
class _FunctionScope:
    body_start: tuple[int, int]
    end: tuple[int, int]
    bound_names: frozenset[str]
    global_names: frozenset[str]
    nonlocal_names: frozenset[str]
    parameter_positions: frozenset[tuple[int, int]]


_IGNORED = {
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.COMMENT,
    tokenize.ENDMARKER,
}


def _replace_names(
    source: str,
    mapping: dict[str, str],
) -> tuple[str, tuple[tuple[str, str, int, int], ...]]:
    tokens: list[tokenize.TokenInfo] = []
    replacements: list[tuple[str, str, int, int]] = []
    reader = io.StringIO(source).readline

    for token in tokenize.generate_tokens(reader):
        if token.type == tokenize.NAME and token.string in mapping:
            replacement = mapping[token.string]
            replacements.append((token.string, replacement, token.start[0], token.start[1] + 1))
            token = tokenize.TokenInfo(
                token.type,
                replacement,
                token.start,
                token.end,
                token.line,
            )
        tokens.append(token)

    return tokenize.untokenize(tokens), tuple(replacements)


def _common_import_path_indices(tokens: list[tokenize.TokenInfo]) -> set[int]:
    """Return NAME-token indices that belong to real Python module paths.

    Common educational identifiers are intentionally broader than a LibraryPack,
    so names such as ``index`` and ``documents`` can be transliterated in normal
    code. They must *not* rewrite package paths such as ``usearch.index`` or
    ``langchain_core.documents`` because those paths are part of Python's actual
    import structure and can collide with class/member transliterations.
    """

    protected: set[int] = set()
    segment: list[int] = []

    def protect_segment(indices: list[int]) -> None:
        significant = [
            index
            for index in indices
            if tokens[index].type not in _IGNORED and tokens[index].string != ";"
        ]
        if not significant:
            return

        first = tokens[significant[0]]
        if first.type != tokenize.NAME:
            return

        if first.string == "from":
            for index in significant[1:]:
                token = tokens[index]
                if token.type == tokenize.NAME and token.string == "import":
                    break
                if token.type == tokenize.NAME:
                    protected.add(index)
            return

        if first.string != "import":
            return

        # In ``import package.path as alias, other.path`` protect only package
        # path segments. Aliases are user identifiers and may be transliterated.
        in_alias = False
        for index in significant[1:]:
            token = tokens[index]
            if token.string == ",":
                in_alias = False
                continue
            if token.type == tokenize.NAME and token.string == "as":
                in_alias = True
                continue
            if token.type == tokenize.NAME and not in_alias:
                protected.add(index)

    for index, token in enumerate(tokens):
        if token.type in {tokenize.NEWLINE, tokenize.ENDMARKER} or token.string == ";":
            protect_segment(segment)
            segment = []
            continue
        segment.append(index)
    protect_segment(segment)
    return protected


def _replace_common_names(
    source: str,
    mapping: dict[str, str],
) -> tuple[str, tuple[tuple[str, str, int, int], ...]]:
    """Replace common identifiers while preserving actual Python import paths."""

    reader = io.StringIO(source).readline
    tokens = list(tokenize.generate_tokens(reader))
    protected = _common_import_path_indices(tokens)
    output_tokens: list[tokenize.TokenInfo] = []
    replacements: list[tuple[str, str, int, int], ...] = []

    for index, token in enumerate(tokens):
        if index not in protected and token.type == tokenize.NAME and token.string in mapping:
            replacement = mapping[token.string]
            replacements.append((token.string, replacement, token.start[0], token.start[1] + 1))
            token = tokenize.TokenInfo(
                token.type,
                replacement,
                token.start,
                token.end,
                token.line,
            )
        output_tokens.append(token)

    return tokenize.untokenize(output_tokens), tuple(replacements)


def _pack_for_module_token(name: str):
    for pack in all_packs():
        if name in {pack.module, pack.kopy_module}:
            return pack
    return None


def _statement_end(tokens: list[tokenize.TokenInfo], start: int) -> int:
    for index in range(start, len(tokens)):
        if tokens[index].type in {tokenize.NEWLINE, tokenize.ENDMARKER}:
            return index
    return len(tokens)


def _significant_indices(tokens: list[tokenize.TokenInfo]) -> list[int]:
    return [i for i, token in enumerate(tokens) if token.type not in _IGNORED]


def _next_significant(
    tokens: list[tokenize.TokenInfo],
    index: int,
    end: int | None = None,
) -> int | None:
    limit = len(tokens) if end is None else min(end, len(tokens))
    for candidate in range(index + 1, limit):
        if tokens[candidate].type not in _IGNORED:
            return candidate
    return None


def _previous_significant(tokens: list[tokenize.TokenInfo], index: int) -> int | None:
    for candidate in range(index - 1, -1, -1):
        if tokens[candidate].type not in _IGNORED:
            return candidate
    return None


def _direct_name_rebindings(
    tokens: list[tokenize.TokenInfo],
    direct_names: dict[str, str],
    common_source_names: set[str],
) -> dict[int, int]:
    """Find module-level simple assignments that shadow a direct pack import.

    Only a true top-level ``name = ...`` rebinding should shadow the imported
    symbol for later module statements. Call keywords (``metric=...``), function
    defaults and local assignments must not poison the module-level direct name.
    Function-local bindings are handled separately from Python lexical scope.
    """

    targets: dict[int, int] = {}
    indent_depth = 0
    bracket_depth = 0
    opening = {"(", "[", "{"}
    closing = {")", "]", "}"}

    for index, token in enumerate(tokens):
        if token.type == tokenize.INDENT:
            indent_depth += 1
            continue
        if token.type == tokenize.DEDENT:
            indent_depth = max(0, indent_depth - 1)
            continue
        if token.type == tokenize.OP:
            if token.string in opening:
                bracket_depth += 1
            elif token.string in closing:
                bracket_depth = max(0, bracket_depth - 1)
            continue

        if (
            indent_depth != 0
            or bracket_depth != 0
            or token.type != tokenize.NAME
            or token.string not in direct_names
            or token.string not in common_source_names
        ):
            continue
        previous = _previous_significant(tokens, index)
        if previous is not None and tokens[previous].string == ".":
            continue
        following = _next_significant(tokens, index)
        if following is not None and tokens[following].string == "=":
            targets[index] = _statement_end(tokens, index)
    return targets


class _LocalBindingCollector(ast.NodeVisitor):
    """Collect names that Python treats as local to one function scope."""

    def __init__(self, root: ast.FunctionDef | ast.AsyncFunctionDef | ast.Lambda):
        self.root = root
        self.bound: set[str] = set()
        self.globals: set[str] = set()
        self.nonlocals: set[str] = set()

    def collect(self) -> tuple[frozenset[str], frozenset[str], frozenset[str]]:
        args = self.root.args
        for arg in (*args.posonlyargs, *args.args, *args.kwonlyargs):
            self.bound.add(arg.arg)
        if args.vararg is not None:
            self.bound.add(args.vararg.arg)
        if args.kwarg is not None:
            self.bound.add(args.kwarg.arg)

        if isinstance(self.root, ast.Lambda):
            self.visit(self.root.body)
        else:
            for statement in self.root.body:
                self.visit(statement)

        self.bound.difference_update(self.globals)
        self.bound.difference_update(self.nonlocals)
        return frozenset(self.bound), frozenset(self.globals), frozenset(self.nonlocals)

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            self.bound.add(node.id)

    def visit_Global(self, node: ast.Global) -> None:
        self.globals.update(node.names)

    def visit_Nonlocal(self, node: ast.Nonlocal) -> None:
        self.nonlocals.update(node.names)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.bound.add(alias.asname or alias.name.split(".", 1)[0])

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for alias in node.names:
            if alias.name != "*":
                self.bound.add(alias.asname or alias.name)

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        if isinstance(node.name, str):
            self.bound.add(node.name)
        for statement in node.body:
            self.visit(statement)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if node is self.root:
            for statement in node.body:
                self.visit(statement)
            return
        self.bound.add(node.name)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        if node is self.root:
            for statement in node.body:
                self.visit(statement)
            return
        self.bound.add(node.name)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.bound.add(node.name)

    def visit_Lambda(self, node: ast.Lambda) -> None:
        if node is self.root:
            self.visit(node.body)

    def visit_ListComp(self, node: ast.ListComp) -> None:
        return

    def visit_SetComp(self, node: ast.SetComp) -> None:
        return

    def visit_DictComp(self, node: ast.DictComp) -> None:
        return

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        return


def _function_scopes(source: str) -> tuple[_FunctionScope, ...]:
    """Describe lexical function scopes so common names can shadow pack classes.

    Direct imports such as ``from ranx import Qrels`` can share a KoPy spelling
    with a learner variable such as ``qrels -> 큐렐즈``. Python decides function
    locals at compile time, not only after a simple ``=`` assignment, so function
    parameters, loop targets, ``with ... as`` bindings, exception names and other
    stores must win over the imported class throughout that function body.
    """

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ()

    scopes: list[_FunctionScope] = []

    class Finder(ast.NodeVisitor):
        def _add(self, node: ast.FunctionDef | ast.AsyncFunctionDef | ast.Lambda) -> None:
            if not hasattr(node, "end_lineno") or node.end_lineno is None:
                return
            bound, globals_, nonlocals = _LocalBindingCollector(node).collect()
            args = node.args
            parameter_positions = {
                (arg.lineno, arg.col_offset)
                for arg in (*args.posonlyargs, *args.args, *args.kwonlyargs)
            }
            if args.vararg is not None:
                parameter_positions.add((args.vararg.lineno, args.vararg.col_offset))
            if args.kwarg is not None:
                parameter_positions.add((args.kwarg.lineno, args.kwarg.col_offset))

            if isinstance(node, ast.Lambda):
                body_start = (node.body.lineno, node.body.col_offset)
            elif node.body:
                body_start = (node.body[0].lineno, node.body[0].col_offset)
            else:
                body_start = (node.lineno, node.col_offset)

            scopes.append(
                _FunctionScope(
                    body_start=body_start,
                    end=(node.end_lineno, node.end_col_offset or 0),
                    bound_names=bound,
                    global_names=globals_,
                    nonlocal_names=nonlocals,
                    parameter_positions=frozenset(parameter_positions),
                )
            )

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            self._add(node)
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            self._add(node)
            self.generic_visit(node)

        def visit_Lambda(self, node: ast.Lambda) -> None:
            self._add(node)
            self.generic_visit(node)

    Finder().visit(tree)
    return tuple(scopes)


def _is_function_shadowed(
    token: tokenize.TokenInfo,
    scopes: tuple[_FunctionScope, ...],
) -> bool:
    """Return whether ``token`` resolves to a common local instead of a pack import."""

    position = token.start
    containing: list[_FunctionScope] = []
    for scope in scopes:
        if position in scope.parameter_positions and token.string in scope.bound_names:
            return True
        if scope.body_start <= position <= scope.end:
            containing.append(scope)

    # Innermost scope first. If it does not bind the name, Python may close over
    # an enclosing function local; a `global` declaration explicitly stops that.
    containing.sort(key=lambda scope: scope.body_start, reverse=True)
    for scope in containing:
        if token.string in scope.global_names:
            return False
        if token.string in scope.bound_names:
            return True
        if token.string in scope.nonlocal_names:
            continue
    return False


def _unique_active_mapping(name: str, active_packs: set[str], reverse: bool) -> str | None:
    targets: set[str] = set()
    for pack in all_packs():
        if pack.name not in active_packs:
            continue
        target = pack.kopy_for(name) if reverse else pack.python_for(name)
        if target is not None:
            targets.add(target)
    if len(targets) == 1:
        return next(iter(targets))
    return None


def _translate_library_packs(
    source: str,
    *,
    reverse: bool,
) -> tuple[str, tuple[tuple[str, str, int, int], ...]]:
    """Translate imported library namespaces without making their words global.

    A library pack becomes active only when its module is imported. Once active,
    module attributes and KoPy-style attributes on objects can use that pack's
    vocabulary. If future packs disagree about one spelling, the ambiguous
    attribute is deliberately left untouched rather than guessed.
    """
    reader = io.StringIO(source).readline
    tokens = list(tokenize.generate_tokens(reader))
    replacements: dict[int, str] = {}
    active_aliases: dict[str, object] = {}
    active_packs: set[str] = set()
    direct_names: dict[str, str] = {}

    # Pass 1: discover imports, activate packs and translate import targets.
    for index, token in enumerate(tokens):
        if token.type != tokenize.NAME:
            continue

        if token.string == "import":
            end = _statement_end(tokens, index + 1)
            cursor = _next_significant(tokens, index, end)
            while cursor is not None and cursor < end:
                module_token = tokens[cursor]
                if module_token.type != tokenize.NAME:
                    cursor = _next_significant(tokens, cursor, end)
                    continue

                pack = _pack_for_module_token(module_token.string)
                if pack is None:
                    # Skip to the next comma-separated import target.
                    while cursor is not None and cursor < end and tokens[cursor].string != ",":
                        cursor = _next_significant(tokens, cursor, end)
                    if cursor is not None:
                        cursor = _next_significant(tokens, cursor, end)
                    continue

                active_packs.add(pack.name)
                replacement = pack.kopy_module if reverse else pack.module
                if module_token.string != replacement:
                    replacements[cursor] = replacement

                # Look for `as alias` before the next comma.
                scan = _next_significant(tokens, cursor, end)
                alias: str | None = None
                while scan is not None and scan < end and tokens[scan].string != ",":
                    if tokens[scan].string == "as":
                        alias_index = _next_significant(tokens, scan, end)
                        if alias_index is not None and tokens[alias_index].type == tokenize.NAME:
                            alias = tokens[alias_index].string
                        break
                    scan = _next_significant(tokens, scan, end)

                if alias:
                    active_aliases[alias] = pack
                else:
                    # Both spellings are understood in source; output uses the
                    # direction-appropriate module spelling.
                    active_aliases[pack.module] = pack
                    active_aliases[pack.kopy_module] = pack

                while cursor is not None and cursor < end and tokens[cursor].string != ",":
                    cursor = _next_significant(tokens, cursor, end)
                if cursor is not None:
                    cursor = _next_significant(tokens, cursor, end)

        elif token.string == "from":
            end = _statement_end(tokens, index + 1)
            module_index = _next_significant(tokens, index, end)
            if module_index is None or tokens[module_index].type != tokenize.NAME:
                continue
            pack = _pack_for_module_token(tokens[module_index].string)
            if pack is None:
                continue

            active_packs.add(pack.name)
            module_replacement = pack.kopy_module if reverse else pack.module
            if tokens[module_index].string != module_replacement:
                replacements[module_index] = module_replacement

            import_index = module_index
            while True:
                import_index = _next_significant(tokens, import_index, end)
                if import_index is None or import_index >= end:
                    break
                if tokens[import_index].string == "import":
                    break
            if import_index is None or import_index >= end:
                continue

            cursor = _next_significant(tokens, import_index, end)
            while cursor is not None and cursor < end:
                member_token = tokens[cursor]
                if member_token.type != tokenize.NAME or member_token.string == "as":
                    cursor = _next_significant(tokens, cursor, end)
                    continue

                target = (
                    pack.kopy_for(member_token.string)
                    if reverse
                    else pack.python_for(member_token.string)
                )
                if target is not None:
                    if member_token.string != target:
                        replacements[cursor] = target
                    next_index = _next_significant(tokens, cursor, end)
                    has_alias = next_index is not None and tokens[next_index].string == "as"
                    if not has_alias:
                        direct_names[member_token.string] = target
                cursor = _next_significant(tokens, cursor, end)

    significant = _significant_indices(tokens)
    sig_position = {token_index: pos for pos, token_index in enumerate(significant)}
    common_source_names = set(COMMON_PY_TO_KO if reverse else COMMON_IDENTIFIERS)
    rebinding_targets = _direct_name_rebindings(tokens, direct_names, common_source_names)
    function_scopes = _function_scopes(source)
    shadow_after: dict[str, int] = {}
    for target_index, statement_end in rebinding_targets.items():
        name = tokens[target_index].string
        current = shadow_after.get(name)
        if current is None or statement_end < current:
            shadow_after[name] = statement_end

    # Pass 2: translate attributes and direct names using only active packs.
    for index, token in enumerate(tokens):
        if token.type != tokenize.NAME:
            continue
        pos = sig_position.get(index)
        if pos is None:
            continue
        previous = tokens[significant[pos - 1]] if pos > 0 else None
        following = tokens[significant[pos + 1]] if pos + 1 < len(significant) else None

        # Bare symbol imported via `from package import symbol`. Common learner
        # identifiers can shadow the same transliteration through assignments or
        # any Python function-local binding (parameters, loop targets, etc.).
        if previous is None or previous.string != ".":
            direct = direct_names.get(token.string)
            shadow_end = shadow_after.get(token.string)
            is_rebinding_target = index in rebinding_targets
            is_shadowed = shadow_end is not None and index >= shadow_end
            is_function_shadow = _is_function_shadowed(token, function_scopes)
            if (
                direct is not None
                and token.string != direct
                and not is_rebinding_target
                and not is_shadowed
                and not is_function_shadow
            ):
                replacements.setdefault(index, direct)

        # Module name used as an attribute-chain root without an alias.
        if following is not None and following.string == "." and token.string in active_aliases:
            pack = active_aliases[token.string]
            target_root = pack.kopy_module if reverse else pack.module
            if token.string in {pack.module, pack.kopy_module} and token.string != target_root:
                replacements.setdefault(index, target_root)

        if previous is None or previous.string != ".":
            continue

        # Find the root of a dotted chain: np.linalg.norm -> np.
        root_pos = pos
        while root_pos >= 2 and tokens[significant[root_pos - 1]].string == ".":
            root_pos -= 2
        root = tokens[significant[root_pos]].string if root_pos < len(significant) else ""
        pack = active_aliases.get(root)

        target: str | None = None
        if pack is not None:
            target = pack.kopy_for(token.string) if reverse else pack.python_for(token.string)
        if target is None:
            # Supports ndarray-style calls such as x.리셰이프(...) while still
            # refusing to guess when multiple active packs disagree.
            target = _unique_active_mapping(token.string, active_packs, reverse)

        if target is not None and token.string != target:
            replacements.setdefault(index, target)

    output_tokens: list[tokenize.TokenInfo] = []
    replacement_log: list[tuple[str, str, int, int]] = []
    for index, token in enumerate(tokens):
        replacement = replacements.get(index)
        if replacement is not None:
            replacement_log.append((token.string, replacement, token.start[0], token.start[1] + 1))
            token = tokenize.TokenInfo(token.type, replacement, token.start, token.end, token.line)
        output_tokens.append(token)

    return tokenize.untokenize(output_tokens), tuple(replacement_log)


def translate(source: str) -> Translation:
    """Translate KoPy source to Python while preserving strings/comments."""
    core_source, core_replacements = _replace_names(source, WORDS)
    pack_source, pack_replacements = _translate_library_packs(core_source, reverse=False)
    python_source, identifier_replacements = _replace_common_names(pack_source, COMMON_IDENTIFIERS)
    return Translation(
        source=source,
        python=python_source,
        replacements=core_replacements + pack_replacements + identifier_replacements,
    )


def to_kopy(source: str) -> ReverseTranslation:
    """Translate Python source to KoPy, including active library packs."""
    pack_source, pack_replacements = _translate_library_packs(source, reverse=True)
    identifier_source, identifier_replacements = _replace_common_names(pack_source, COMMON_PY_TO_KO)
    kopy_source, core_replacements = _replace_names(identifier_source, PY_TO_KO)
    return ReverseTranslation(
        source=source,
        kopy=kopy_source,
        replacements=pack_replacements + identifier_replacements + core_replacements,
    )
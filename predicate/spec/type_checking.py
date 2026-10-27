"""Resolve names that a module only imports under ``if TYPE_CHECKING:``.

Annotations such as ``x: dt.timedelta`` fail with ``NameError`` when ``dt`` is only imported for the type checker.
This module re-runs the imports and simple type aliases from those blocks into a separate namespace, which is then
used as ``localns`` when resolving type hints. Nothing else from the block is executed.
"""

import ast
import importlib
import importlib.util
import inspect
import sys
from collections.abc import Callable, Iterator
from functools import cache
from types import ModuleType
from typing import Any


def _is_type_checking_test(test: ast.expr) -> bool:
    match test:
        case ast.Name(id="TYPE_CHECKING") | ast.Attribute(attr="TYPE_CHECKING"):
            return True
        case _:
            return False


def _type_checking_statements(tree: ast.Module) -> Iterator[ast.stmt]:
    # Only module-level blocks: nested ones (in functions or classes) don't affect module globals
    for node in tree.body:
        if isinstance(node, ast.If) and _is_type_checking_test(node.test):
            yield from node.body


def _resolve_module(node: ast.ImportFrom, module: ModuleType) -> str:
    if not node.level:
        return node.module or ""
    package = module.__package__ or module.__name__
    return importlib.util.resolve_name("." * node.level + (node.module or ""), package)


def _import(node: ast.Import, namespace: dict[str, Any]) -> None:
    for alias in node.names:
        imported = importlib.import_module(alias.name)
        if alias.asname:
            namespace[alias.asname] = imported
        else:
            # `import a.b` binds `a`
            top = alias.name.partition(".")[0]
            namespace[top] = importlib.import_module(top)


def _import_from(node: ast.ImportFrom, module: ModuleType, namespace: dict[str, Any]) -> None:
    source = importlib.import_module(_resolve_module(node, module))
    for alias in (alias for alias in node.names if alias.name != "*"):
        name = alias.asname or alias.name
        try:
            namespace[name] = getattr(source, alias.name)
        except AttributeError:
            # `from pkg import submodule`
            namespace[name] = importlib.import_module(f"{source.__name__}.{alias.name}")


# Node types a type expression like `dict[str, int | None]` or `t.Optional["X"]` is built from; no calls, lambdas etc.
_TYPE_EXPRESSION_NODES: tuple[type[ast.AST], ...] = (
    ast.Name,
    ast.Attribute,
    ast.Subscript,
    ast.Tuple,
    ast.List,
    ast.BinOp,
    ast.BitOr,
    ast.Constant,
    ast.Load,
    ast.Expression,
)


def _is_type_expression(node: ast.expr) -> bool:
    return all(isinstance(child, _TYPE_EXPRESSION_NODES) for child in ast.walk(ast.Expression(body=node)))


def _alias(node: ast.Assign | ast.AnnAssign, module: ModuleType, namespace: dict[str, Any]) -> None:
    # Simple aliases only, e.g. `NumberOrString: TypeAlias = float | str`; anything that could call code is skipped
    match node:
        case (
            ast.Assign(targets=[ast.Name(id=name)], value=value) | ast.AnnAssign(target=ast.Name(id=name), value=value)
        ) if value is not None and _is_type_expression(value):
            expression = ast.Expression(body=value)
            namespace[name] = eval(compile(expression, module.__name__, "eval"), vars(module) | namespace)  # noqa: S307


def _run(statement: ast.stmt, module: ModuleType, namespace: dict[str, Any]) -> None:
    match statement:
        case ast.Import():
            _import(statement, namespace)
        case ast.ImportFrom():
            _import_from(statement, module, namespace)
        case ast.Assign() | ast.AnnAssign():
            _alias(statement, module, namespace)


@cache
def _namespace_for_module(module_name: str) -> dict[str, Any]:
    module = sys.modules.get(module_name)
    if module is None:
        return {}
    try:
        tree = ast.parse(inspect.getsource(module))
    except (OSError, TypeError, SyntaxError):
        return {}  # no source available, e.g. a C extension or a frozen module

    namespace: dict[str, Any] = {}
    for statement in _type_checking_statements(tree):
        _run_if_possible(statement, module, namespace)
    return namespace


def _run_if_possible(statement: ast.stmt, module: ModuleType, namespace: dict[str, Any]) -> None:
    try:
        _run(statement, module, namespace)
    except Exception:  # noqa: BLE001
        # ponytail: skip what doesn't import at runtime (e.g. _typeshed); those names stay unresolved
        return


def type_checking_namespace(f: Callable) -> dict[str, Any]:
    """Return the names f's module only imports under ``if TYPE_CHECKING:``, or {} if there are none."""
    module_name = getattr(f, "__module__", None)
    return _namespace_for_module(module_name) if module_name else {}

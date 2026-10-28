"""Resolve names that a module only imports under ``if TYPE_CHECKING:``.

Annotations such as ``x: dt.timedelta`` fail with ``NameError`` when ``dt`` is only imported for the type checker.
This module re-runs the imports and simple type aliases from those blocks into a separate namespace, which is then
used as ``localns`` when resolving type hints. Nothing else from the block is executed.
"""

import ast
import builtins
import contextlib
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
            # `from pkg import submodule`; a name that doesn't exist at runtime is skipped, the others still import
            with contextlib.suppress(ImportError):
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


def _is_type_var_call(node: ast.expr) -> bool:
    # `TypeVar("T", bound=...)` or `t.TypeVar(...)`: no side effects when every argument is a type expression
    match node:
        case ast.Call(func=ast.Name(id="TypeVar") | ast.Attribute(attr="TypeVar"), args=[ast.Constant(str()), *rest]):
            return all(_is_type_expression(arg) for arg in [*rest, *(keyword.value for keyword in node.keywords)])
        case _:
            return False


def _alias(node: ast.Assign | ast.AnnAssign, module: ModuleType, namespace: dict[str, Any]) -> None:
    # Simple aliases and TypeVars only, e.g. `NumberOrString: TypeAlias = float | str`; other calls are skipped
    match node:
        case (
            ast.Assign(targets=[ast.Name(id=name)], value=value) | ast.AnnAssign(target=ast.Name(id=name), value=value)
        ) if value is not None and (_is_type_expression(value) or _is_type_var_call(value)):
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
def _parse(module_name: str) -> tuple[ModuleType, ast.Module] | None:
    module = sys.modules.get(module_name)
    if module is None:
        return None
    try:
        return module, ast.parse(inspect.getsource(module))
    except (OSError, TypeError, SyntaxError):
        return None  # no source available, e.g. a C extension or a frozen module


@cache
def _namespace_for_module(module_name: str) -> dict[str, Any]:
    if (parsed := _parse(module_name)) is None:
        return {}
    module, tree = parsed
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


def _module_name(f: Callable) -> str | None:
    # The defining module, not __module__: libraries rewrite that to the public package (e.g. pandas' @set_module)
    return getattr(inspect.unwrap(f), "__globals__", {}).get("__name__") or getattr(f, "__module__", None)


def type_checking_namespace(f: Callable) -> dict[str, Any]:
    """Return the names f's module only imports under ``if TYPE_CHECKING:``, or {} if there are none."""
    module_name = _module_name(f)
    return _namespace_for_module(module_name) if module_name else {}


def _imported_from(module_name: str) -> Iterator[str]:
    if (parsed := _parse(module_name)) is None:
        return
    module, tree = parsed
    statements = [*tree.body, *_type_checking_statements(tree)]
    yield from (_resolve_module(node, module) for node in statements if isinstance(node, ast.ImportFrom))


def imported_namespace(f: Callable) -> dict[str, Any]:
    """Like type_checking_namespace, plus the globals and TYPE_CHECKING names of every module f's module imports from.

    An alias like ``PolarsDataType = Union["DataTypeClass", "DataType"]`` holds quoted names that resolve in its own
    module (its globals or its TYPE_CHECKING imports), not in f's. Builtins and f's own module take precedence, so
    e.g. ``polars.list`` doesn't shadow ``list``.
    """
    if not (module_name := _module_name(f)):
        return {}
    namespaces = (_module_namespace(name) for name in _imported_from(module_name))
    borrowed = {k: v for namespace in namespaces for k, v in namespace.items() if k not in vars(builtins)}
    return borrowed | _module_namespace(module_name)


def _module_namespace(module_name: str) -> dict[str, Any]:
    module = sys.modules.get(module_name)
    return (vars(module) if module else {}) | _namespace_for_module(module_name)

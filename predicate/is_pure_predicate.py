import ast
import builtins
from functools import cache, reduce
from inspect import getclosurevars, getsourcefile, getsourcelines, isfunction
from pathlib import Path
from sys import stdlib_module_names
from textwrap import dedent
from types import FunctionType
from typing import Any, Final, NamedTuple

from predicate.function_predicate import fn_p
from predicate.predicate import Predicate

_CATEGORIES: Final = {
    "io": ["open", "print", "input", "subprocess", "logging", "shutil", "socket"],
    "system": ["os", "sys"],
    "randomness": ["random"],
    "time": ["time"],
    "dynamic-code": ["exec", "eval", "compile", "__import__"],
}
_CATEGORY_OF: Final = {name: category for category, names in _CATEGORIES.items() for name in names}
_NO_SOURCE: Final = "no-source"  # category of functions we can't analyze; not an impurity of the callee


class Impurity(NamedTuple):
    """Why a function looks impure."""

    category: str  # io, system, randomness, time, dynamic-code, global-state or no-source
    reason: str  # short description with file:line of the (root) cause


def _root_name(node: ast.expr) -> str | None:
    while isinstance(node, ast.Attribute):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _describe_impurity(node: ast.AST) -> tuple[str, str] | None:
    """Return (category, description) if the node is an obvious impurity."""
    match node:
        case ast.Global():
            return "global-state", "global statement"
        case ast.Nonlocal():
            return "global-state", "nonlocal statement"
        case ast.Call(func=ast.Name(id=name)) if name in _CATEGORY_OF:
            return _CATEGORY_OF[name], f"calls {name}"
        case ast.Call(func=ast.Attribute() as func) if (root := _root_name(func)) in _CATEGORY_OF:
            return _CATEGORY_OF[root], f"calls {_dotted_name(func)}"
        case ast.Call(func=ast.Attribute(attr="now" | "utcnow" | "today") as func):  # datetime(...) itself is pure
            return "time", f"calls {_dotted_name(func)}"
        case _:
            return None


def _dotted_name(node: ast.expr) -> str | None:
    match node:
        case ast.Name(id=name):
            return name
        case ast.Attribute(value=value, attr=attr):
            prefix = _dotted_name(value)
            return prefix and f"{prefix}.{attr}"
        case _:
            return None


def _resolve(fn: FunctionType, dotted: str) -> Any:
    name, *attrs = dotted.split(".")
    scope = {**vars(builtins), **fn.__globals__, **getclosurevars(fn).nonlocals}
    try:
        return reduce(getattr, attrs, scope[name])
    except (KeyError, AttributeError):  # locals, parameters, dynamic attributes: unknown, not impure
        return None


def _callee_impurity(fn: FunctionType, dotted: str) -> Impurity | None:
    callee = _resolve(fn, dotted)
    skip = (
        not isfunction(callee)
        or callee in _in_progress  # recursion
        or callee.__module__.split(".")[0] in stdlib_module_names  # the name lists cover the stdlib
    )
    impurity = None if skip else _impurity(callee)
    return None if impurity and impurity.category == _NO_SOURCE else impurity


def _compute_impurity(fn: Any) -> Impurity | None:
    """None if fn (and the functions it calls) look pure, otherwise the category and a short reason with file:line."""
    try:
        lines, start = getsourcelines(fn)
        tree = ast.parse(dedent("".join(lines)))
    except (OSError, TypeError, SyntaxError):  # no source: builtins, C extensions, REPL
        return Impurity(_NO_SOURCE, "no source available")

    def where(node: Any) -> str:
        return f"{Path(getsourcefile(fn) or '?').name}:{start + node.lineno - 1}"

    nodes = list(ast.walk(tree))
    direct = [
        (node.lineno, Impurity(category, f"{description} ({where(node)})"))  # type: ignore[attr-defined]
        for node in nodes
        if (found := _describe_impurity(node))
        for category, description in [found]
    ]
    if direct:
        return min(direct, key=lambda d: d[0])[1]
    if not isfunction(fn):
        return None
    calls = sorted(
        ((node, name) for node in nodes if isinstance(node, ast.Call) and (name := _dotted_name(node.func))),
        key=lambda call: (call[0].lineno, call[0].col_offset),
    )
    _in_progress.add(fn)
    try:
        return next(
            (
                Impurity(impurity.category, f"calls {name} ({where(node)}) -> {impurity.reason.rsplit(' -> ', 1)[-1]}")
                for node, name in calls  # first hop and root cause
                if (impurity := _callee_impurity(fn, name))
            ),
            None,
        )
    finally:
        _in_progress.discard(fn)


# ponytail: a result cached while inside a recursion cycle assumed the cycle pure; clear_purity_cache() if that matters
_in_progress: set[FunctionType] = set()
_impurity = cache(_compute_impurity)


def clear_purity_cache() -> None:
    _impurity.cache_clear()


def find_impurity(fn: Any) -> Impurity | None:
    """None if fn looks pure, otherwise the category and reason of the first impurity found."""
    return (_impurity if isfunction(fn) else _compute_impurity)(fn)


def _is_pure(fn: Any) -> bool:
    return find_impurity(fn) is None


is_pure_p: Final[Predicate[Any]] = fn_p(fn=_is_pure)
"""Heuristic: True for a function with no global/nonlocal, no obvious I/O or impure calls, in itself or in the
non-stdlib functions it calls (transitively). Unresolvable calls are not considered impure."""

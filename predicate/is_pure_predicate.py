import ast
from inspect import getsource
from textwrap import dedent
from typing import Any, Final

from predicate.function_predicate import fn_p
from predicate.predicate import Predicate

_IMPURE_BUILTINS: Final = {"open", "print", "input", "exec", "eval", "compile", "__import__"}
_IMPURE_MODULES: Final = {"os", "sys", "random", "time", "datetime", "subprocess", "logging", "shutil", "socket"}


def _root_name(node: ast.expr) -> str | None:
    while isinstance(node, ast.Attribute):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _is_impure_node(node: ast.AST) -> bool:
    match node:
        case ast.Global() | ast.Nonlocal():
            return True
        case ast.Call(func=ast.Name(id=name)):
            return name in _IMPURE_BUILTINS or name in _IMPURE_MODULES
        case ast.Call(func=ast.Attribute() as func):
            return _root_name(func) in _IMPURE_MODULES
        case _:
            return False


def _is_pure(fn: Any) -> bool:
    # ponytail: heuristic on source text; no call graph or parameter-mutation check, add when #453 needs it
    try:
        tree = ast.parse(dedent(getsource(fn)))
    except (OSError, TypeError, SyntaxError):  # no source: builtins, C extensions, REPL
        return False
    return not any(_is_impure_node(node) for node in ast.walk(tree))


is_pure_p: Final[Predicate[Any]] = fn_p(fn=_is_pure)
"""Heuristic: True for a function whose source has no global/nonlocal and no obvious I/O or impure calls."""

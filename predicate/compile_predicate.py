"""Compile predicates to native Python callables for faster evaluation."""

import ast
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from typing import override

from predicate.predicate import Predicate


class NotCompilableError(Exception):
    """Raised when a predicate cannot be compiled to a native callable."""


@dataclass
class CompiledPredicate[T](Predicate[T]):
    """A predicate that delegates evaluation to a compiled native callable.

    Preserves full introspection (repr, count, explain_failure, contains) via
    the wrapped predicate. Only __call__ is replaced with the compiled fast path.
    """

    predicate: Predicate[T]
    fn: Callable[[T], bool] = field(compare=False, repr=False)

    def __call__(self, x: T) -> bool:
        return self.fn(x)

    def __repr__(self) -> str:
        return repr(self.predicate)

    def __contains__(self, p: object) -> bool:
        return p in self.predicate  # type: ignore[operator]

    @override
    @property
    def count(self) -> int:
        return self.predicate.count

    @override
    def explain_failure(self, x: T) -> dict:
        return self.predicate.explain_failure(x)

    @override
    def get_klass(self) -> type:
        return self.predicate.klass


def _to_ast(predicate: Predicate, namespace: dict) -> ast.expr:  # noqa: C901
    from predicate.eq_predicate import EqPredicate
    from predicate.ge_predicate import GePredicate
    from predicate.gt_predicate import GtPredicate
    from predicate.in_predicate import InPredicate
    from predicate.is_falsy_predicate import IsFalsyPredicate
    from predicate.is_instance_predicate import IsInstancePredicate
    from predicate.is_none_predicate import IsNonePredicate
    from predicate.is_not_none_predicate import IsNotNonePredicate
    from predicate.is_truthy_predicate import IsTruthyPredicate
    from predicate.le_predicate import LePredicate
    from predicate.lt_predicate import LtPredicate
    from predicate.ne_predicate import NePredicate
    from predicate.not_in_predicate import NotInPredicate
    from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, XorPredicate
    from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate

    x = ast.Name(id="x", ctx=ast.Load())

    def _const(v) -> ast.Constant:
        return ast.Constant(value=v)

    def _cmp(ops: list, comparators: list) -> ast.Compare:
        return ast.Compare(left=x, ops=ops, comparators=comparators)

    def _delegate(p: Predicate) -> ast.Call:
        key = f"_p{len(namespace)}"
        namespace[key] = p
        return ast.Call(func=ast.Name(id=key, ctx=ast.Load()), args=[x], keywords=[])

    match predicate:
        case EqPredicate(v):
            return _cmp([ast.Eq()], [_const(v)])
        case NePredicate(v):
            return _cmp([ast.NotEq()], [_const(v)])
        case GtPredicate(v):
            return _cmp([ast.Gt()], [_const(v)])
        case GePredicate(v):
            return _cmp([ast.GtE()], [_const(v)])
        case LtPredicate(v):
            return _cmp([ast.Lt()], [_const(v)])
        case LePredicate(v):
            return _cmp([ast.LtE()], [_const(v)])
        case IsNonePredicate():
            return _cmp([ast.Is()], [_const(None)])
        case IsNotNonePredicate():
            return _cmp([ast.IsNot()], [_const(None)])
        case IsTruthyPredicate():
            return ast.Call(func=ast.Name(id="bool", ctx=ast.Load()), args=[x], keywords=[])
        case IsFalsyPredicate():
            return ast.UnaryOp(
                op=ast.Not(),
                operand=ast.Call(func=ast.Name(id="bool", ctx=ast.Load()), args=[x], keywords=[]),
            )
        case InPredicate(v) if isinstance(v, Iterable):
            key = f"_s{len(namespace)}"
            namespace[key] = frozenset(v)
            return _cmp([ast.In()], [ast.Name(id=key, ctx=ast.Load())])
        case NotInPredicate(v) if isinstance(v, Iterable):
            key = f"_s{len(namespace)}"
            namespace[key] = frozenset(v)
            return _cmp([ast.NotIn()], [ast.Name(id=key, ctx=ast.Load())])
        case GeLePredicate(lower, upper):
            return ast.Compare(left=_const(lower), ops=[ast.LtE(), ast.LtE()], comparators=[x, _const(upper)])
        case GeLtPredicate(lower, upper):
            return ast.Compare(left=_const(lower), ops=[ast.LtE(), ast.Lt()], comparators=[x, _const(upper)])
        case GtLePredicate(lower, upper):
            return ast.Compare(left=_const(lower), ops=[ast.Lt(), ast.LtE()], comparators=[x, _const(upper)])
        case GtLtPredicate(lower, upper):
            return ast.Compare(left=_const(lower), ops=[ast.Lt(), ast.Lt()], comparators=[x, _const(upper)])
        case IsInstancePredicate():
            # Delegate to preserve special bool/int and generic-type semantics.
            return _delegate(predicate)
        case AndPredicate(left, right):
            return ast.BoolOp(op=ast.And(), values=[_to_ast(left, namespace), _to_ast(right, namespace)])
        case OrPredicate(left, right):
            return ast.BoolOp(op=ast.Or(), values=[_to_ast(left, namespace), _to_ast(right, namespace)])
        case NotPredicate(p):
            return ast.UnaryOp(op=ast.Not(), operand=_to_ast(p, namespace))
        case XorPredicate(left, right):
            # bool(left_expr) ^ bool(right_expr)
            bool_left = ast.Call(func=ast.Name(id="bool", ctx=ast.Load()), args=[_to_ast(left, namespace)], keywords=[])
            bool_right = ast.Call(
                func=ast.Name(id="bool", ctx=ast.Load()), args=[_to_ast(right, namespace)], keywords=[]
            )
            return ast.BinOp(left=bool_left, op=ast.BitXor(), right=bool_right)
        case _:
            raise NotCompilableError(f"Cannot compile predicate of type {type(predicate).__name__}")


def compile_predicate[T](predicate: Predicate[T]) -> CompiledPredicate[T]:
    """Compile a predicate to a native callable for faster evaluation.

    Raises NotCompilableError for unsupported predicate types (all_p, any_p, fn_p, regex_p, etc.).
    """
    namespace: dict = {}
    body = _to_ast(predicate, namespace)

    lambda_ast = ast.Expression(
        body=ast.Lambda(
            args=ast.arguments(
                posonlyargs=[],
                args=[ast.arg(arg="x")],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=body,
        )
    )
    ast.fix_missing_locations(lambda_ast)
    fn = eval(compile(lambda_ast, "<compiled_predicate>", "eval"), namespace)  # noqa: S307
    return CompiledPredicate(predicate=predicate, fn=fn)


def try_compile_predicate[T](predicate: Predicate[T]) -> Predicate[T]:
    """Compile a predicate if possible, otherwise return the original unchanged."""
    try:
        return compile_predicate(predicate)
    except NotCompilableError:
        return predicate

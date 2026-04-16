"""Compile predicates to native Python callables for faster evaluation."""

import ast
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from functools import singledispatch
from typing import override

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.comp_predicate import CompPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.in_predicate import InPredicate
from predicate.is_close_predicate import IsClosePredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.lt_predicate import LtPredicate
from predicate.named_predicate import NamedPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate, XorPredicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.tuple_of_predicate import TupleOfPredicate


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


def _x() -> ast.Name:
    return ast.Name(id="x", ctx=ast.Load())


def _const(v) -> ast.Constant:
    return ast.Constant(value=v)


def _cmp(ops: list, comparators: list) -> ast.Compare:
    return ast.Compare(left=_x(), ops=ops, comparators=comparators)


def _delegate(predicate: Predicate, namespace: dict) -> ast.Call:
    key = f"_p{len(namespace)}"
    namespace[key] = predicate
    return ast.Call(func=ast.Name(id=key, ctx=ast.Load()), args=[_x()], keywords=[])


@singledispatch
def _to_ast(predicate: Predicate, namespace: dict) -> ast.expr:
    raise NotCompilableError(f"Cannot compile predicate of type {type(predicate).__name__}")


@_to_ast.register
def _(predicate: AlwaysTruePredicate, namespace: dict) -> ast.expr:
    return _const(True)


@_to_ast.register
def _(predicate: AlwaysFalsePredicate, namespace: dict) -> ast.expr:
    return _const(False)


@_to_ast.register
def _(predicate: NamedPredicate, namespace: dict) -> ast.expr:
    return _const(predicate.v)


@_to_ast.register
def _(predicate: EqPredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.Eq()], [_const(predicate.v)])


@_to_ast.register
def _(predicate: NePredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.NotEq()], [_const(predicate.v)])


@_to_ast.register
def _(predicate: GtPredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.Gt()], [_const(predicate.v)])


@_to_ast.register
def _(predicate: GePredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.GtE()], [_const(predicate.v)])


@_to_ast.register
def _(predicate: LtPredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.Lt()], [_const(predicate.v)])


@_to_ast.register
def _(predicate: LePredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.LtE()], [_const(predicate.v)])


@_to_ast.register
def _(predicate: IsNonePredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.Is()], [_const(None)])


@_to_ast.register
def _(predicate: IsNotNonePredicate, namespace: dict) -> ast.expr:
    return _cmp([ast.IsNot()], [_const(None)])


@_to_ast.register
def _(predicate: IsTruthyPredicate, namespace: dict) -> ast.expr:
    return ast.Call(func=ast.Name(id="bool", ctx=ast.Load()), args=[_x()], keywords=[])


@_to_ast.register
def _(predicate: IsFalsyPredicate, namespace: dict) -> ast.expr:
    return ast.UnaryOp(
        op=ast.Not(),
        operand=ast.Call(func=ast.Name(id="bool", ctx=ast.Load()), args=[_x()], keywords=[]),
    )


@_to_ast.register
def _(predicate: InPredicate, namespace: dict) -> ast.expr:
    if not isinstance(predicate.v, Iterable):
        raise NotCompilableError(f"Cannot compile InPredicate with non-iterable value {predicate.v!r}")
    key = f"_s{len(namespace)}"
    namespace[key] = frozenset(predicate.v)
    return _cmp([ast.In()], [ast.Name(id=key, ctx=ast.Load())])


@_to_ast.register
def _(predicate: NotInPredicate, namespace: dict) -> ast.expr:
    if not isinstance(predicate.v, Iterable):
        raise NotCompilableError(f"Cannot compile NotInPredicate with non-iterable value {predicate.v!r}")
    key = f"_s{len(namespace)}"
    namespace[key] = frozenset(predicate.v)
    return _cmp([ast.NotIn()], [ast.Name(id=key, ctx=ast.Load())])


@_to_ast.register
def _(predicate: HasKeyPredicate, namespace: dict) -> ast.expr:
    key = f"_k{len(namespace)}"
    namespace[key] = predicate.key
    return ast.Compare(
        left=ast.Name(id=key, ctx=ast.Load()),
        ops=[ast.In()],
        comparators=[_x()],
    )


@_to_ast.register
def _(predicate: GeLePredicate, namespace: dict) -> ast.expr:
    return ast.Compare(
        left=_const(predicate.lower), ops=[ast.LtE(), ast.LtE()], comparators=[_x(), _const(predicate.upper)]
    )


@_to_ast.register
def _(predicate: GeLtPredicate, namespace: dict) -> ast.expr:
    return ast.Compare(
        left=_const(predicate.lower), ops=[ast.LtE(), ast.Lt()], comparators=[_x(), _const(predicate.upper)]
    )


@_to_ast.register
def _(predicate: GtLePredicate, namespace: dict) -> ast.expr:
    return ast.Compare(
        left=_const(predicate.lower), ops=[ast.Lt(), ast.LtE()], comparators=[_x(), _const(predicate.upper)]
    )


@_to_ast.register
def _(predicate: GtLtPredicate, namespace: dict) -> ast.expr:
    return ast.Compare(
        left=_const(predicate.lower), ops=[ast.Lt(), ast.Lt()], comparators=[_x(), _const(predicate.upper)]
    )


@_to_ast.register
def _(predicate: IsInstancePredicate, namespace: dict) -> ast.expr:
    # Delegate to preserve special bool/int and generic-type semantics.
    return _delegate(predicate, namespace)


@_to_ast.register
def _(predicate: AndPredicate, namespace: dict) -> ast.expr:
    return ast.BoolOp(op=ast.And(), values=[_to_ast(predicate.left, namespace), _to_ast(predicate.right, namespace)])


@_to_ast.register
def _(predicate: OrPredicate, namespace: dict) -> ast.expr:
    return ast.BoolOp(op=ast.Or(), values=[_to_ast(predicate.left, namespace), _to_ast(predicate.right, namespace)])


@_to_ast.register
def _(predicate: NotPredicate, namespace: dict) -> ast.expr:
    return ast.UnaryOp(op=ast.Not(), operand=_to_ast(predicate.predicate, namespace))


@_to_ast.register
def _(predicate: XorPredicate, namespace: dict) -> ast.expr:
    # bool(left_expr) ^ bool(right_expr)
    bool_left = ast.Call(
        func=ast.Name(id="bool", ctx=ast.Load()), args=[_to_ast(predicate.left, namespace)], keywords=[]
    )
    bool_right = ast.Call(
        func=ast.Name(id="bool", ctx=ast.Load()), args=[_to_ast(predicate.right, namespace)], keywords=[]
    )
    return ast.BinOp(left=bool_left, op=ast.BitXor(), right=bool_right)


@_to_ast.register
def _(predicate: AllPredicate, namespace: dict) -> ast.expr:
    return _any_all_ast(predicate, "all", namespace)


def _any_all_ast(predicate: AllPredicate | AnyPredicate, fn_name: str, namespace: dict) -> ast.expr:
    try:
        inner_fn = compile_predicate(predicate.predicate).fn
    except NotCompilableError:
        inner_fn = predicate.predicate

    inner_key = f"_p{len(namespace)}"
    namespace[inner_key] = inner_fn

    loop_var = "_e"
    gen = ast.GeneratorExp(
        elt=ast.Call(
            func=ast.Name(id=inner_key, ctx=ast.Load()),
            args=[ast.Name(id=loop_var, ctx=ast.Load())],
            keywords=[],
        ),
        generators=[
            ast.comprehension(
                target=ast.Name(id=loop_var, ctx=ast.Store()),
                iter=_x(),
                ifs=[],
                is_async=0,
            )
        ],
    )
    return ast.Call(func=ast.Name(id=fn_name, ctx=ast.Load()), args=[gen], keywords=[])


@_to_ast.register
def _(predicate: AnyPredicate, namespace: dict) -> ast.expr:
    return _any_all_ast(predicate, "any", namespace)


def _isinstance_and_all_ast(predicate: Predicate, type_name: str, namespace: dict) -> ast.expr:
    isinstance_check = ast.Call(
        func=ast.Name(id="isinstance", ctx=ast.Load()),
        args=[_x(), ast.Name(id=type_name, ctx=ast.Load())],
        keywords=[],
    )
    all_check = _any_all_ast(predicate, "all", namespace)
    return ast.BoolOp(op=ast.And(), values=[isinstance_check, all_check])


@_to_ast.register
def _(predicate: ListOfPredicate, namespace: dict) -> ast.expr:
    return _isinstance_and_all_ast(predicate, "list", namespace)


@_to_ast.register
def _(predicate: SetOfPredicate, namespace: dict) -> ast.expr:
    return _isinstance_and_all_ast(predicate, "set", namespace)


@_to_ast.register
def _(predicate: IsClosePredicate, namespace: dict) -> ast.expr:
    import math

    namespace["_isclose"] = math.isclose
    return ast.Call(
        func=ast.Name(id="_isclose", ctx=ast.Load()),
        args=[_x(), _const(predicate.target)],
        keywords=[
            ast.keyword(arg="rel_tol", value=_const(predicate.rel_tol)),
            ast.keyword(arg="abs_tol", value=_const(predicate.abs_tol)),
        ],
    )


@_to_ast.register
def _(predicate: CompPredicate, namespace: dict) -> ast.expr:
    try:
        inner_fn = compile_predicate(predicate.predicate).fn
    except NotCompilableError:
        inner_fn = predicate.predicate
    fn_key = f"_fn{len(namespace)}"
    namespace[fn_key] = predicate.fn
    p_key = f"_p{len(namespace)}"
    namespace[p_key] = inner_fn
    return ast.Call(
        func=ast.Name(id=p_key, ctx=ast.Load()),
        args=[ast.Call(func=ast.Name(id=fn_key, ctx=ast.Load()), args=[_x()], keywords=[])],
        keywords=[],
    )


@_to_ast.register
def _(predicate: TupleOfPredicate, namespace: dict) -> ast.expr:
    n = len(predicate.predicates)
    len_check = ast.Compare(
        left=ast.Call(func=ast.Name(id="len", ctx=ast.Load()), args=[_x()], keywords=[]),
        ops=[ast.Eq()],
        comparators=[_const(n)],
    )
    if n == 0:
        return len_check

    element_checks = []
    for i, p in enumerate(predicate.predicates):
        try:
            inner_fn = compile_predicate(p).fn
        except NotCompilableError:
            inner_fn = p
        key = f"_p{len(namespace)}"
        namespace[key] = inner_fn
        element_checks.append(
            ast.Call(
                func=ast.Name(id=key, ctx=ast.Load()),
                args=[ast.Subscript(value=_x(), slice=_const(i), ctx=ast.Load())],
                keywords=[],
            )
        )
    return ast.BoolOp(op=ast.And(), values=[len_check, *element_checks])


def compile_predicate[T](predicate: Predicate[T]) -> CompiledPredicate[T]:
    """Compile a predicate to a native callable for faster evaluation.

    Raises NotCompilableError for unsupported predicate types (fn_p, regex_p, etc.).
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

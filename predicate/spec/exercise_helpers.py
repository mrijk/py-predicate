import sys
import types
from inspect import Signature, isroutine, signature
from itertools import islice, repeat
from typing import Any, Callable, Literal, TypeGuard, TypeVar, Union, get_args, get_origin, get_type_hints

from more_itertools import take

from predicate import always_true_p, generate_true, is_instance_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.explain import explain
from predicate.frozendict_of_predicate import is_frozendict_of_p
from predicate.frozenset_of_predicate import is_frozenset_of_p
from predicate.implies import implies
from predicate.in_predicate import in_p
from predicate.is_none_predicate import is_none_p
from predicate.list_of_predicate import is_list_of_p
from predicate.or_predicate import or_p
from predicate.predicate import Predicate
from predicate.set_of_predicate import is_set_of_p
from predicate.spec.spec import InvalidSpecError, Spec, SpecViolationError
from predicate.tuple_of_predicate import is_tuple_of_p

_type_narrowing_origins: set = {TypeGuard}
if sys.version_info >= (3, 13):  # pragma: no cover
    from typing import TypeIs

    _type_narrowing_origins.add(TypeIs)

_union_origins: set = {Union, types.UnionType}


def resolved_signature(f: Callable) -> Signature:
    # get_type_hints also resolves nested string annotations, e.g. x: "str" under `from __future__ import annotations`
    sig = signature(f)
    # Python < 3.14 get_type_hints rejects callable instances, so read the hints from their __call__
    hints = get_type_hints(f if isroutine(f) else type(f).__call__)
    parameters = [p.replace(annotation=hints.get(name, p.annotation)) for name, p in sig.parameters.items()]
    return sig.replace(parameters=parameters, return_annotation=hints.get("return", sig.return_annotation))


def annotation_to_predicate(annotation: Any) -> Predicate:  # noqa: C901
    if annotation is None:
        return is_none_p
    if annotation is Any:
        return always_true_p
    if type(annotation) is TypeVar:
        return always_true_p
    origin = get_origin(annotation)
    if origin in _type_narrowing_origins:
        return always_true_p  # TypeGuard/TypeIs is bool at runtime
    if origin in _union_origins:
        return or_p(*[annotation_to_predicate(t) for t in get_args(annotation)])
    if origin is Literal:
        return in_p(get_args(annotation))
    if origin is list:
        (item_type,) = get_args(annotation)
        return is_list_of_p(annotation_to_predicate(item_type))
    if origin is set:
        (item_type,) = get_args(annotation)
        return is_set_of_p(annotation_to_predicate(item_type))
    if origin is frozenset:
        (item_type,) = get_args(annotation)
        return is_frozenset_of_p(annotation_to_predicate(item_type))
    if origin is dict:
        key_type, value_type = get_args(annotation)
        return is_dict_of_p((annotation_to_predicate(key_type), annotation_to_predicate(value_type)))
    if sys.version_info >= (3, 15) and origin is frozendict:  # noqa: F821
        key_type, value_type = get_args(annotation)
        return is_frozendict_of_p((annotation_to_predicate(key_type), annotation_to_predicate(value_type)))
    if origin is tuple:
        args = get_args(annotation)
        if args and args[-1] is not Ellipsis:
            return is_tuple_of_p(*[annotation_to_predicate(t) for t in args])
    return is_instance_p(annotation)


def get_return_predicate(sig: Signature) -> Predicate:
    return annotation_to_predicate(sig.return_annotation)


def validate_args(f: Callable, spec: Spec) -> dict[str, Predicate]:
    parameters = spec["args"]
    sig = resolved_signature(f)

    for key, _ in parameters.items():
        if key not in sig.parameters:
            raise InvalidSpecError(f"Parameter '{key}' not in function signature")

    return parameters


def get_return_spec(f: Callable, spec: Spec) -> Spec:
    if not spec.get("ret"):
        sig = resolved_signature(f)

        if sig.return_annotation == sig.empty:
            raise InvalidSpecError("Return annotation not in spec")
        return spec | {"ret": is_instance_p(sig.return_annotation)}
    return spec


def check_signature_against_spec(f: Callable, spec: Spec) -> Spec:

    sig = resolved_signature(f)

    parameters = validate_args(f, spec)

    spec = get_return_spec(f, spec)

    for key in sig.parameters:
        parameter = sig.parameters[key]
        annotation = parameter.annotation
        if annotation == parameter.empty:
            if key not in parameters:
                raise InvalidSpecError(f"Unannotated parameter '{key}' not in spec")
        elif type(annotation) is TypeVar:
            if key not in parameters:
                raise InvalidSpecError(f"Unannotated parameter '{key}' not in spec")
        else:
            annotation_p = is_instance_p(annotation)
            if key not in parameters:
                parameters[key] = annotation_p
            else:
                if not implies(parameters[key], annotation_p):
                    raise InvalidSpecError("Spec predicate is not a constrained annotation")

    return spec


def generate_values(spec: Spec, n: int) -> tuple:
    parameters = spec["args"]
    return_p = spec["ret"]
    if predicates := tuple(parameters.items()):
        candidates = generate_true(is_dict_of_p(*predicates))
        if pre := spec.get("pre"):
            max_attempts = 100 * n
            candidates = (value for value in islice(candidates, max_attempts) if pre(**value))
            values = take(n, candidates)
            if len(values) < n:
                raise InvalidSpecError(f"Could not generate values satisfying pre after {max_attempts} attempts")
        else:
            values = take(n, candidates)
    else:
        values = take(n, repeat({}))
    return return_p, values


def verify_result(spec: Spec, return_p: Predicate, value: dict, result) -> None:
    if not return_p(result):
        raise SpecViolationError(f"Not conform spec: {explain(return_p, result)}")

    if fn := spec.get("fn"):
        if not fn(**value, ret=result):
            raise SpecViolationError(f"Not conform spec: fn constraint failed for inputs {value} -> {result}")

    if fn_p := spec.get("fn_p"):
        fn_p_result = fn_p(**value)
        if not fn_p_result(result):
            raise SpecViolationError(f"Not conform spec: {explain(fn_p_result, result)}")


def check_exception(spec: Spec, value: dict, exc: Exception) -> Exception:
    expected = spec.get("raises")
    if not expected:
        raise exc
    if not isinstance(exc, expected):
        raise SpecViolationError(
            f"Not conform spec: unexpected exception {type(exc).__name__} for inputs {value}"
        ) from exc
    return exc

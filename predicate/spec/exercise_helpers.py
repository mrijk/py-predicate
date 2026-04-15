import sys
import types
from inspect import Signature, signature
from itertools import repeat
from typing import Any, Callable, Literal, TypeGuard, TypeVar, Union, get_args, get_origin

from more_itertools import take

from predicate import always_true_p, generate_true, is_instance_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.explain import explain
from predicate.implies import implies
from predicate.in_predicate import in_p
from predicate.is_none_predicate import is_none_p
from predicate.list_of_predicate import is_list_of_p
from predicate.predicate import Predicate, or_p
from predicate.set_of_predicate import is_set_of_p
from predicate.spec.spec import Spec
from predicate.tuple_of_predicate import is_tuple_of_p

_type_narrowing_origins: set = {TypeGuard}
if sys.version_info >= (3, 13):  # pragma: no cover
    from typing import TypeIs

    _type_narrowing_origins.add(TypeIs)

_union_origins: set = {Union, types.UnionType}


def annotation_to_predicate(annotation: Any) -> Predicate:
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
    if origin is dict:
        key_type, value_type = get_args(annotation)
        return is_dict_of_p((annotation_to_predicate(key_type), annotation_to_predicate(value_type)))
    if origin is tuple:
        args = get_args(annotation)
        if args and args[-1] is not Ellipsis:
            return is_tuple_of_p(*[annotation_to_predicate(t) for t in args])
    return is_instance_p(annotation)


def get_return_predicate(sig: Signature) -> Predicate:
    return annotation_to_predicate(sig.return_annotation)


def validate_args(f: Callable, spec: Spec) -> dict[str, Predicate]:
    parameters = spec["args"]
    sig = signature(f)

    for key, _ in parameters.items():
        if key not in sig.parameters:
            raise AssertionError(f"Parameter '{key}' not in function signature")

    return parameters


def get_return_spec(f: Callable, spec: Spec) -> Spec:
    if not spec.get("ret"):
        sig = signature(f)

        if sig.return_annotation == sig.empty:
            raise AssertionError("Return annotation not in spec")
        return spec | {"ret": is_instance_p(sig.return_annotation)}
    return spec


def check_signature_against_spec(f: Callable, spec: Spec) -> Spec:
    from inspect import signature

    sig = signature(f)

    parameters = validate_args(f, spec)

    spec = get_return_spec(f, spec)

    for key in sig.parameters:
        parameter = sig.parameters[key]
        annotation = parameter.annotation
        if annotation == parameter.empty:
            if key not in parameters:
                raise AssertionError(f"Unannotated parameter '{key}' not in spec")
        elif type(annotation) is TypeVar:
            if key not in parameters:
                raise AssertionError(f"Unannotated parameter '{key}' not in spec")
        else:
            annotation_p = is_instance_p(annotation)
            if key not in parameters:
                parameters[key] = annotation_p
            else:
                if not implies(parameters[key], annotation_p):
                    raise AssertionError("Spec predicate is not a constrained annotation")

    return spec


def generate_values(spec: Spec, n: int) -> tuple:
    parameters = spec["args"]
    return_p = spec["ret"]
    if predicates := tuple(parameters.items()):
        values = take(n, generate_true(is_dict_of_p(*predicates)))
    else:
        values = take(n, repeat({}))
    return return_p, values


def verify_result(spec: Spec, return_p: Predicate, value: dict, result) -> None:
    if not return_p(result):
        raise AssertionError(f"Not conform spec: {explain(return_p, result)}")

    if fn := spec.get("fn"):
        if not fn(**value, ret=result):
            raise AssertionError(f"Not conform spec: fn constraint failed for inputs {value} -> {result}")

    if fn_p := spec.get("fn_p"):
        fn_p_result = fn_p(**value)
        if not fn_p_result(result):
            raise AssertionError(f"Not conform spec: {explain(fn_p_result, result)}")

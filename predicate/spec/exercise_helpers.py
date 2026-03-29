import sys
from inspect import Signature
from itertools import repeat
from typing import Callable, TypeGuard, TypeVar, get_origin

from more_itertools import take

from predicate import always_true_p, generate_true, is_instance_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.explain import explain
from predicate.implies import implies
from predicate.predicate import Predicate
from predicate.spec.spec import Spec

_type_narrowing_origins: set = {TypeGuard}
if sys.version_info >= (3, 13):
    from typing import TypeIs

    _type_narrowing_origins.add(TypeIs)


def get_return_predicate(sig: Signature) -> Predicate:
    annotation = sig.return_annotation
    if type(annotation) is TypeVar:
        return always_true_p
    if get_origin(annotation) in _type_narrowing_origins:
        return always_true_p  # TypeGuard/TypeIs is bool at runtime
    return is_instance_p(annotation)


def check_signature_against_spec(f: Callable, spec: Spec):
    from inspect import signature

    sig = signature(f)

    parameters = spec["args"]
    for key, _ in parameters.items():
        if key not in sig.parameters:
            raise AssertionError(f"Parameter '{key}' not in function signature")

    if not spec.get("ret"):
        if sig.return_annotation == sig.empty:
            raise AssertionError("Return annotation not in spec")
        spec["ret"] = is_instance_p(sig.return_annotation)

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


def _generate_values(spec: Spec, n: int) -> tuple:
    parameters = spec["args"]
    return_p = spec["ret"]
    if predicates := tuple(parameters.items()):
        values = take(n, generate_true(is_dict_of_p(*predicates)))
    else:
        values = take(n, repeat({}))
    return return_p, values


def _verify_result(spec: Spec, return_p: Predicate, value: dict, result) -> None:
    if not return_p(result):
        raise AssertionError(f"Not conform spec: {explain(return_p, result)}")

    if fn := spec.get("fn"):
        if not fn(**value, ret=result):
            raise AssertionError("Not conform spec, details tbd")

    if fn_p := spec.get("fn_p"):
        fn_p_result = fn_p(**value)
        if not fn_p_result(result):
            raise AssertionError(f"Not conform spec: {explain(fn_p_result, result)}")

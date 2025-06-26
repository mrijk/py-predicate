from collections.abc import Iterator
from inspect import signature
from typing import Callable

from more_itertools import take

from predicate import explain, generate_true, is_instance_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.spec.spec import Spec


def get_spec_from_annotation(f: Callable) -> Spec | None:
    sig = signature(f)

    if sig.return_annotation == sig.empty:
        return None

    spec: Spec = {"args": {}, "ret": is_instance_p(sig.return_annotation)}

    for key in sig.parameters:
        parameter = sig.parameters[key]
        if parameter.annotation == parameter.empty:
            return None

        spec["args"][key] = is_instance_p(parameter.annotation)

    return spec


def check_signature_against_spec(f: Callable, spec: Spec):
    sig = signature(f)

    parameters = spec["args"]
    for key, _ in parameters.items():
        if key not in sig.parameters:
            raise AssertionError(f"Parameter '{key}' not in function signature")

    # TODO: all parameters that are not annotated, should be in the spec

    if sig.return_annotation == sig.empty and not spec.get("ret"):
        raise AssertionError("Return annotation not in spec")

    for key in sig.parameters:
        parameter = sig.parameters[key]
        if parameter.annotation == parameter.empty:
            if key not in parameters:
                raise AssertionError(f"Unannotated parameter '{key}' not in spec")


def exercise(f: Callable, spec: Spec | None = None, n: int = 10) -> Iterator[tuple]:
    if not spec:
        if not (spec_from_annotation := get_spec_from_annotation(f)):
            raise ValueError("Not implemented yet")
        spec = spec_from_annotation
    else:
        check_signature_against_spec(f, spec)

    parameters = spec["args"]
    return_p = spec["ret"]

    predicates = tuple(parameters.items())
    predicate = is_dict_of_p(*predicates)

    values = take(n, generate_true(predicate))

    for value in values:
        result = f(**value)
        if not return_p(result):
            raise AssertionError(f"Not conform spec: {explain(return_p, result)}")

        if fn := spec.get("fn"):
            if not fn(**value, ret=result):
                raise AssertionError("Not conform spec, details tbd")

        if fn_p := spec.get("fn_p"):
            fn_p_result = fn_p(**value)
            if not fn_p_result(result):
                raise AssertionError("Not conform spec, details tbd")

        yield tuple(value.values()), result

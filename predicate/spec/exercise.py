from inspect import Parameter, Signature, signature
from itertools import repeat
from types import FunctionType
from typing import Callable, Iterator, TypeVar

from more_itertools import take

from predicate import always_true_p, generate_true, is_instance_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.explain import explain
from predicate.implies import implies
from predicate.predicate import Predicate
from predicate.spec.spec import Spec


def get_return_predicate(sig: Signature) -> Predicate:
    annotation = sig.return_annotation
    if type(annotation) is TypeVar:
        return always_true_p
    return is_instance_p(annotation)


def get_spec_from_class_annotation(f: Callable) -> Spec | None:
    sig = signature(f.__call__)  # type: ignore

    if sig.return_annotation == sig.empty:
        return None

    spec: Spec = {"args": {}, "ret": get_return_predicate(sig)}

    parameters = {key: sig.parameters[key] for key in sig.parameters if key != "self"}

    for key in parameters:
        parameter = parameters[key]
        annotation = parameter.annotation

        if annotation == parameter.empty:
            if parameter.kind == Parameter.VAR_POSITIONAL:
                continue

            if parameter.kind == Parameter.VAR_KEYWORD:
                continue

            return None

        if isinstance(f, Predicate):
            try:
                spec["args"][key] = is_instance_p(f.klass)
            except NotImplementedError:  # TODO this is ugly!
                spec["args"][key] = always_true_p
        elif type(annotation) is TypeVar:
            spec["args"][key] = always_true_p
        else:
            spec["args"][key] = is_instance_p(annotation)

    return spec


def get_spec_from_function_annotation(f: Callable) -> Spec | None:
    sig = signature(f)

    if sig.return_annotation == sig.empty:
        return None

    spec: Spec = {"args": {}, "ret": get_return_predicate(sig)}

    for key in sig.parameters:
        parameter = sig.parameters[key]
        annotation = parameter.annotation

        if annotation == parameter.empty:
            return None
        if type(annotation) is TypeVar:
            spec["args"][key] = always_true_p
        else:
            spec["args"][key] = is_instance_p(annotation)

    return spec


def check_signature_against_spec(f: Callable, spec: Spec):
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


def exercise(f: Callable, spec: Spec | None = None, n: int = 10) -> Iterator[tuple]:
    if isinstance(f, FunctionType):
        yield from exercise_function(f, spec, n)
    else:
        yield from exercise_class(f, spec, n)


def exercise_class(f: Callable, spec: Spec | None, n: int) -> Iterator[tuple]:
    if not spec:
        if not (spec_from_annotation := get_spec_from_class_annotation(f)):
            raise ValueError("Not implemented yet")
        spec = spec_from_annotation
    else:
        check_signature_against_spec(f, spec)

    parameters = spec["args"]
    return_p = spec["ret"]

    if predicates := tuple(parameters.items()):
        predicate = is_dict_of_p(*predicates)

        values = take(n, generate_true(predicate))
    else:
        values = take(n, repeat({}))

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


def exercise_function(f: Callable, spec: Spec | None, n: int) -> Iterator[tuple]:
    if not spec:
        if not (spec_from_annotation := get_spec_from_function_annotation(f)):
            raise ValueError("Not implemented yet")
        spec = spec_from_annotation
    else:
        check_signature_against_spec(f, spec)

    parameters = spec["args"]
    return_p = spec["ret"]

    if predicates := tuple(parameters.items()):
        predicate = is_dict_of_p(*predicates)

        values = take(n, generate_true(predicate))
    else:
        values = take(n, repeat({}))

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

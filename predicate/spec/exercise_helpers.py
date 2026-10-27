import collections.abc
import sys
import types
from functools import reduce
from inspect import Parameter, Signature, isroutine, signature
from itertools import islice, repeat, takewhile
from typing import (
    Any,
    Callable,
    Iterator,
    Literal,
    LiteralString,
    Never,
    NoReturn,
    Tuple,
    TypeGuard,
    TypeVar,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

from more_itertools import first, take

from predicate import all_p, always_false_p, always_true_p, generate_true, is_instance_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.explain import explain
from predicate.frozendict_of_predicate import is_frozendict_of_p
from predicate.frozenset_of_predicate import is_frozenset_of_p
from predicate.has_length_predicate import is_empty_p
from predicate.implies import implies
from predicate.in_predicate import in_p
from predicate.is_instance_predicate import is_dict_p, is_str_p, is_tuple_p
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

# Abstract collections whose single type argument is the item type; typing.Sequence etc. have the same origins
_item_collection_origins: set = {
    collections.abc.Collection,
    collections.abc.MutableSequence,
    collections.abc.MutableSet,
    collections.abc.Sequence,
    collections.abc.Set,
}
_mapping_origins: set = {collections.abc.Mapping, collections.abc.MutableMapping}


def resolved_signature(f: Callable) -> Signature:
    # get_type_hints also resolves nested string annotations, e.g. x: "str" under `from __future__ import annotations`
    sig = signature(f)
    # Python < 3.14 get_type_hints rejects callable instances, so read the hints from their __call__
    hints = get_type_hints(f if isroutine(f) else type(f).__call__)
    parameters = [p.replace(annotation=hints.get(name, p.annotation)) for name, p in sig.parameters.items()]
    return sig.replace(parameters=parameters, return_annotation=hints.get("return", sig.return_annotation))


def annotation_to_predicate(annotation: Any) -> Predicate:  # noqa: C901
    if annotation is None or annotation is types.NoneType:
        return is_none_p
    if annotation in (Any, object):
        return always_true_p  # every value is an object
    if type(annotation) is TypeVar:
        return always_true_p
    if annotation in (Never, NoReturn):
        return always_false_p  # no value inhabits Never
    if annotation is LiteralString:
        return is_str_p  # literal-ness is not observable at runtime
    if annotation is float:
        return is_instance_p(float, int)  # PEP 484 numeric tower: int is acceptable for float
    if annotation is complex:
        return is_instance_p(complex, float, int)
    origin = get_origin(annotation)
    if origin in _type_narrowing_origins:
        return always_true_p  # TypeGuard/TypeIs is bool at runtime
    if origin in _union_origins:
        return reduce(or_p, [annotation_to_predicate(t) for t in get_args(annotation)])
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
        # is_dict_of_p rejects {}, but dict[K, V] includes the empty dict
        return is_dict_p & (
            is_empty_p | is_dict_of_p((annotation_to_predicate(key_type), annotation_to_predicate(value_type)))
        )
    if origin in _item_collection_origins:
        (item_type,) = get_args(annotation)
        return is_instance_p(annotation) & all_p(annotation_to_predicate(item_type))
    if origin in _mapping_origins:
        key_type, value_type = get_args(annotation)
        return is_instance_p(annotation) & (
            is_empty_p | is_dict_of_p((annotation_to_predicate(key_type), annotation_to_predicate(value_type)))
        )
    if sys.version_info >= (3, 15) and origin is frozendict:  # noqa: F821
        key_type, value_type = get_args(annotation)
        return is_frozendict_of_p((annotation_to_predicate(key_type), annotation_to_predicate(value_type)))
    if origin is tuple:
        match get_args(annotation):
            case () if annotation is not Tuple:  # tuple[()]; bare typing.Tuple also has no args
                return is_tuple_p & is_empty_p
            case (item_type, types.EllipsisType()):
                return is_tuple_p & all_p(annotation_to_predicate(item_type))
            case (_, *_) as item_types:
                return is_tuple_of_p(*[annotation_to_predicate(t) for t in item_types])
    return is_instance_p(annotation)


def get_return_predicate(sig: Signature) -> Predicate:
    return annotation_to_predicate(sig.return_annotation)


def ret_name(spec: Spec) -> str:
    return spec.get("ret_name", "ret")


def check_ret_name(sig: Signature, spec: Spec) -> None:
    if "fn" in spec and (name := ret_name(spec)) in sig.parameters:
        raise InvalidSpecError(f"Parameter '{name}' clashes with the fn return value name, set 'ret_name' in the spec")


def validate_args(f: Callable, spec: Spec) -> dict[str, Predicate]:
    # Copy, so filling in annotation predicates doesn't change the caller's spec
    parameters = dict(spec["args"])
    sig = resolved_signature(f)
    check_ret_name(sig, spec)

    if (key := first((key for key in parameters if key not in sig.parameters), None)) is not None:
        raise InvalidSpecError(f"Parameter '{key}' not in function signature")

    return parameters


def get_return_spec(f: Callable, spec: Spec) -> Spec:
    if not spec.get("ret"):
        sig = resolved_signature(f)

        if sig.return_annotation == sig.empty:
            raise InvalidSpecError("Return annotation not in spec")
        return spec | {"ret": annotation_to_predicate(sig.return_annotation)}
    return spec


def check_signature_against_spec(f: Callable, spec: Spec) -> Spec:

    sig = resolved_signature(f)

    parameters = validate_args(f, spec)

    spec = get_return_spec(f, spec) | {"args": parameters}

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
            annotation_p = param_predicate(parameter)
            if key not in parameters:
                parameters[key] = annotation_p
            else:
                if not implies(parameters[key], annotation_p):
                    raise InvalidSpecError("Spec predicate is not a constrained annotation")

    return spec


def param_predicate(param: Parameter) -> Predicate:
    predicate = annotation_to_predicate(param.annotation)
    match param.kind:
        case Parameter.VAR_POSITIONAL:
            return all_p(predicate)
        case Parameter.VAR_KEYWORD:
            return is_dict_p & (is_empty_p | is_dict_of_p((is_str_p, predicate)))
        case _:
            return predicate


_positional_kinds = (Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD, Parameter.VAR_POSITIONAL)


def _positional_values(param: Parameter, arg) -> Iterator:
    yield from arg if param.kind == Parameter.VAR_POSITIONAL else [arg]


def _keyword_items(param: Parameter, arg) -> Iterator[tuple[str, Any]]:
    yield from arg.items() if param.kind == Parameter.VAR_KEYWORD else [(param.name, arg)]


def call_args(sig: Signature, value: dict) -> tuple[list, dict]:
    # Leading parameters go positionally (in signature order) so *args and positional-only parameters bind correctly
    positional = list(
        takewhile(lambda param: param.name in value and param.kind in _positional_kinds, sig.parameters.values())
    )
    keyword = [param for param in list(sig.parameters.values())[len(positional) :] if param.name in value]
    args = [arg for param in positional for arg in _positional_values(param, value[param.name])]
    kwargs = dict(item for param in keyword for item in _keyword_items(param, value[param.name]))
    return args, kwargs


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


def verify_result(spec: Spec, return_p: Predicate, value: dict, result: Any) -> None:
    if not return_p(result):
        raise SpecViolationError(f"Not conform spec: {explain(return_p, result)}")

    if fn := spec.get("fn"):
        if not fn(**value, **{ret_name(spec): result}):
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


def no_spec_error(name: str, missing: str) -> InvalidSpecError:
    return InvalidSpecError(f"Cannot derive spec for '{name}': {missing}; pass a Spec or annotate it")

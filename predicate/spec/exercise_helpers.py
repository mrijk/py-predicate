import collections.abc
import inspect
import io
import sys
import types
import warnings
from functools import partial, reduce
from inspect import Parameter, Signature, isroutine, signature
from itertools import islice, repeat, takewhile
from typing import (
    IO,
    Annotated,
    Any,
    BinaryIO,
    Callable,
    Final,
    ForwardRef,
    Iterator,
    Literal,
    LiteralString,
    Never,
    NewType,
    NoReturn,
    NotRequired,
    Required,
    TextIO,
    Tuple,
    TypeAliasType,
    TypeGuard,
    TypeVar,
    Union,
    Unpack,
    get_args,
    get_origin,
    get_type_hints,
)

from more_itertools import first, take

from predicate import all_p, always_false_p, always_true_p, generate_true, is_instance_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.eq_predicate import eq_p
from predicate.explain import explain
from predicate.fn_predicate import fn_p
from predicate.frozendict_of_predicate import is_frozendict_of_p
from predicate.frozenset_of_predicate import is_frozenset_of_p
from predicate.generator.helpers import random_named_tuple_classes, random_typed_dict_classes
from predicate.has_length_predicate import is_empty_p
from predicate.implies import implies
from predicate.in_predicate import in_p
from predicate.is_instance_predicate import is_dict_p, is_str_p, is_tuple_p
from predicate.is_named_tuple_predicate import is_named_tuple_class
from predicate.is_none_predicate import is_none_p
from predicate.is_subclass_predicate import is_subclass_p
from predicate.list_of_predicate import is_list_of_p
from predicate.or_predicate import or_p
from predicate.predicate import Predicate
from predicate.set_of_predicate import is_set_of_p
from predicate.spec.spec import InvalidSpecError, Spec, SpecViolationError, UnresolvedAnnotationWarning
from predicate.spec.type_checking import (
    imported_namespace,
    imported_namespace_for_module,
    resolve_forward_ref,
    type_checking_namespace,
)
from predicate.struct_predicate import is_struct_p
from predicate.tuple_of_predicate import is_tuple_of_p
from predicate.type_var_predicate import ConstrainedTypeVarPredicate, FreeTypeVarPredicate

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
    collections.abc.Reversible,
    collections.abc.Sequence,
    collections.abc.Set,
}
_mapping_origins: set = {collections.abc.Mapping, collections.abc.MutableMapping}


def _signature(f: Callable) -> Signature:
    if sys.version_info >= (3, 14):  # pragma: no cover
        from annotationlib import Format

        # On 3.14 annotations are evaluated lazily, so a name that only exists under TYPE_CHECKING raises here too
        return signature(f, annotation_format=Format.FORWARDREF)
    return signature(f)  # pragma: no cover


def _forward_refs(hint: Any) -> Iterator[ForwardRef]:
    # Also nested ones, e.g. int | ForwardRef("Fraction") from an alias in another module
    if isinstance(hint, ForwardRef):
        yield hint
    for arg in get_args(hint):
        yield from _forward_refs(arg)


def _type_hints(owner: Callable, localns: dict[str, Any]) -> dict[str, Any]:
    if sys.version_info >= (3, 14):  # pragma: no cover
        from annotationlib import Format

        hints = get_type_hints(owner, localns=localns, format=Format.FORWARDREF)
        # Names that are still unresolved raise NameError here; resolved_signature then falls back per annotation
        for ref in (ref for hint in hints.values() for ref in _forward_refs(hint)):
            ref.evaluate(locals=localns)
        return hints
    return get_type_hints(owner, localns=localns)  # pragma: no cover


def _hints_or_any(owner: Callable, localns: dict[str, Any]) -> dict[str, Any]:
    """Resolve each annotation on its own; one that can't be evaluated at runtime becomes Any, with a warning (#292)."""
    annotations = _raw_annotations(owner)
    hints: dict[str, Any] = {}
    for name in annotations:
        probe = types.FunctionType(_empty_code, {}, name)  # a function with just this one annotation
        probe.__annotations__ = {name: annotations[name]}
        probe.__module__ = owner.__module__
        probe.__globals__.update(getattr(inspect.unwrap(owner), "__globals__", {}))
        try:
            hints |= _type_hints(probe, localns)
        except (NameError, TypeError, AttributeError) as e:
            hints[name] = Any
            _warn_unresolved(owner, name, e)
    return hints


def _warn_unresolved(owner: Callable, name: str, error: Exception) -> None:
    message = f"Annotation of {name!r} in {owner.__qualname__} can't be evaluated at runtime ({error}); treated as Any"
    _warn(message, getattr(inspect.unwrap(owner), "__code__", None), owner.__module__)


def _warn(message: str, code: types.CodeType | None, module: str) -> None:
    # Attributed to the function's own source line; the registry makes the default filter show it once per message
    warnings.warn_explicit(
        message,
        UnresolvedAnnotationWarning,
        filename=code.co_filename if code else module,
        lineno=code.co_firstlineno if code else 0,
        module=module,
        registry=_unresolved_warning_registry,
    )


_unresolved_warning_registry: dict = {}


def _raw_annotations(owner: Callable) -> dict[str, Any]:
    if sys.version_info >= (3, 14):  # pragma: no cover
        from annotationlib import Format, get_annotations

        # Reading __annotations__ evaluates them on 3.14; FORWARDREF keeps unresolvable ones as ForwardRef
        return dict(get_annotations(owner, format=Format.FORWARDREF))
    return dict(getattr(owner, "__annotations__", {}))  # pragma: no cover


def _empty() -> None: ...


_empty_code = _empty.__code__


def callable_name(f: Callable) -> str:
    """Return a name for any callable, e.g. for a partial or an instance of a class with __call__ (#362)."""
    if isinstance(f, partial):
        return callable_name(f.func)
    return getattr(f, "__name__", type(f).__name__)


def resolved_signature(f: Callable) -> Signature:
    # get_type_hints also resolves nested string annotations, e.g. x: "str" under `from __future__ import annotations`
    sig = _signature(f)
    # Python < 3.14 get_type_hints rejects callable instances, so read the hints from their __call__
    owner = f if isroutine(f) else type(f).__call__
    # Names the module only imports under `if TYPE_CHECKING:` are re-imported into localns
    try:
        hints = _type_hints(owner, type_checking_namespace(owner))
    except NameError:
        try:
            # A quoted name inside an alias imported from another module, e.g. Union["DataTypeClass", ...] (#333)
            hints = _type_hints(owner, imported_namespace(owner))
        except (NameError, TypeError, AttributeError):
            hints = _hints_or_any(owner, imported_namespace(owner))
    except (TypeError, AttributeError):
        # e.g. classmethod[Any, Any, Any]: only subscriptable for type checkers before 3.14
        hints = _hints_or_any(owner, imported_namespace(owner))
    parameters = [p.replace(annotation=hints.get(name, p.annotation)) for name, p in sig.parameters.items()]
    return sig.replace(parameters=parameters, return_annotation=hints.get("return", sig.return_annotation))


def _resolve_or_any(ref: str | ForwardRef, module_name: str, owner: str) -> Any:
    try:
        return resolve_forward_ref(ref, module_name)
    except (NameError, TypeError, AttributeError) as e:
        # e.g. a TypeVar bound to a class that only exists under TYPE_CHECKING
        text = ref.__forward_arg__ if isinstance(ref, ForwardRef) else ref
        _warn(f"{text!r} in {owner} can't be evaluated at runtime ({e}); treated as Any", None, module_name)
        return Any


def _type_arg_class(arg: Any, module_name: str, owner: str) -> Any:
    if isinstance(arg, str | ForwardRef):
        arg = _resolve_or_any(arg, module_name, owner)
    if arg is None:
        return types.NoneType
    if arg is Any:
        return object
    return get_origin(arg) or arg  # Function[Any] -> Function


def _type_arg_classes(arg: Any) -> tuple[Any, ...]:
    """Return the classes type[arg] stands for: a TypeVar's constraints or bound (else object), or arg itself."""
    if isinstance(arg, TypeVar):
        classes = arg.__constraints__ or (arg.__bound__ or object,)
        owner = f"the bound of TypeVar {arg.__name__}"
        return tuple(_type_arg_class(klass, arg.__module__, owner) for klass in _flatten_unions(classes))
    return tuple(_type_arg_class(klass, "", "a type[...] annotation") for klass in _flatten_unions((arg,)))


def _type_var_annotation(type_var: TypeVar) -> Any:
    """Return what a plain TypeVar stands for: the union of its constraints, its bound, or Any."""
    classes = type_var.__constraints__ or (type_var.__bound__ or Any,)
    resolved = [
        _resolve_or_any(c, type_var.__module__, f"the bound of TypeVar {type_var.__name__}")
        if isinstance(c, str | ForwardRef)
        else c
        for c in classes
    ]
    return Union[tuple(resolved)]  # noqa: UP007  Union of a tuple; a single member stays itself


def _type_var_predicate(type_var: TypeVar) -> Predicate:
    """Return a predicate for a value within T's bound or constraints (binding T to other arguments is #258)."""
    if type_var.__constraints__:
        union = _type_var_annotation(type_var)
        constraints = get_args(union) if get_origin(union) in _union_origins else (union,)
        return reduce(ConstrainedTypeVarPredicate, [annotation_to_predicate(c) for c in constraints])
    if type_var.__bound__ is None:
        return FreeTypeVarPredicate()
    return annotation_to_predicate(_type_var_annotation(type_var))


# typing.NamedTuple and typing.TypedDict are functions at runtime: issubclass() and __subclasses__() reject them
_named_tuple_class_p: Final[Predicate] = fn_p(is_named_tuple_class, generate_true_fn=random_named_tuple_classes)


def is_typed_dict_class(klass: Any) -> bool:
    # typing.is_typeddict doesn't recognise typing_extensions.TypedDict classes before Python 3.14
    return isinstance(klass, type) and issubclass(klass, dict) and hasattr(klass, "__required_keys__")


_typed_dict_class_p: Final[Predicate] = fn_p(is_typed_dict_class, generate_true_fn=random_typed_dict_classes)


def _is_typing_special(klass: Any, name: str) -> bool:
    # typing.TypedDict and typing_extensions.TypedDict are different objects
    return getattr(klass, "__name__", None) == name and getattr(klass, "__module__", None) in (
        "typing",
        "typing_extensions",
    )


def type_arg_predicate(arg: Any) -> Predicate:
    """Return the predicate for the classes type[arg] stands for (without checking that the value is a class)."""
    match _type_arg_classes(arg):
        case (klass,) if _is_typing_special(klass, "NamedTuple"):
            return _named_tuple_class_p
        case (klass,) if _is_typing_special(klass, "TypedDict"):
            return _typed_dict_class_p
        case classes:
            return is_subclass_p(classes)


def _flatten_unions(classes: tuple[Any, ...]) -> Iterator[Any]:
    # A union inside type[...] stands for each of its members
    for klass in classes:
        if get_origin(klass) in _union_origins:
            yield from _flatten_unions(get_args(klass))
        else:
            yield klass


def _io_predicate(annotation: Any) -> Predicate | None:
    # typing.IO classes are for type checkers only: io.BytesIO() isn't an instance of typing.IO, but is an io.IOBase
    if annotation is BinaryIO or annotation == IO[bytes]:
        return is_instance_p(io.IOBase) & ~is_instance_p(io.TextIOBase)  # SpooledTemporaryFile isn't BufferedIOBase
    if annotation is TextIO or annotation == IO[str]:
        return is_instance_p(io.TextIOBase)
    if annotation is IO or get_origin(annotation) is IO:
        return is_instance_p(io.IOBase)
    return None


_typed_dicts_in_progress: set[type] = set()


def _typed_dict_keys(klass: type, hints: dict[str, Any]) -> tuple[set[str], set[str]]:
    # Under `from __future__ import annotations` the class can't see NotRequired[...] in its string annotations, so
    # __required_keys__ lists those keys as required; read Required / NotRequired from the resolved hints instead
    optional = set(klass.__optional_keys__)  # type: ignore[attr-defined]
    optional |= {key for key, hint in hints.items() if get_origin(hint) is NotRequired}
    optional -= {key for key, hint in hints.items() if get_origin(hint) is Required}
    return set(hints) - optional, optional


def class_hints(klass: type, include_extras: bool = False) -> dict[str, Any]:
    """Return the field annotations of a TypedDict or NamedTuple; ones that can't be evaluated become Any (#292)."""
    localns = type_checking_namespace(klass)
    try:
        return get_type_hints(klass, localns=localns, include_extras=include_extras)
    except (NameError, TypeError, AttributeError):
        module = sys.modules.get(klass.__module__)
        globalns = imported_namespace_for_module(klass.__module__) | (vars(module) if module else {})
        return {
            name: _class_hint(klass, name, raw, globalns | localns, include_extras)
            for name, raw in _raw_annotations(klass).items()
        }


def _class_hint(klass: type, name: str, raw: Any, namespace: dict[str, Any], include_extras: bool) -> Any:
    probe = types.SimpleNamespace(__annotations__={name: raw}, __module__=klass.__module__, __mro__=())
    try:
        return get_type_hints(probe, globalns=namespace, include_extras=include_extras)[name]
    except (NameError, TypeError, AttributeError) as e:
        _warn(
            f"Annotation of field {name!r} in {klass.__qualname__} can't be evaluated at runtime ({e}); treated as Any",
            None,
            klass.__module__,
        )
        return Any


def _typed_dict_predicate(klass: type) -> Predicate:
    # ponytail: extra keys are rejected (like a dict literal for a type checker); a TypedDict subtype passed for its
    # base would fail. A recursive reference (children: list["Node"]) is only checked to be a dict.
    if klass in _typed_dicts_in_progress:
        return is_dict_p
    _typed_dicts_in_progress.add(klass)
    try:
        required, optional = _typed_dict_keys(klass, class_hints(klass, include_extras=True))
        hints = class_hints(klass)  # without Required / NotRequired / Annotated
        predicates = {key: annotation_to_predicate(hint) for key, hint in hints.items()}
    finally:
        _typed_dicts_in_progress.discard(klass)
    return is_struct_p(
        required={key: predicates[key] for key in required}, optional={key: predicates[key] for key in optional}
    )


def _unwrap_alias(annotation: Any) -> Any:
    """Return the type behind NewType, Annotated and PEP 695 `type` aliases, which isinstance() can't check."""
    match annotation:
        case NewType():
            return _unwrap_alias(annotation.__supertype__)
        case TypeAliasType():
            return _unwrap_alias(annotation.__value__)
        case _ if get_origin(annotation) is Annotated:
            return _unwrap_alias(
                annotation.__origin__
            )  # ponytail: the metadata (e.g. annotated-types bounds) is ignored
        case _ if isinstance(get_origin(annotation), TypeAliasType):
            # A generic alias such as G[int] with `type G[T] = list[T]`
            alias = get_origin(annotation)
            return _unwrap_alias(alias.__value__[get_args(annotation)] if alias.__type_params__ else alias.__value__)
        case _:
            return annotation


def annotation_to_predicate(annotation: Any) -> Predicate:  # noqa: C901
    annotation = _unwrap_alias(annotation)
    if annotation is None or annotation is types.NoneType:
        return is_none_p
    if is_typed_dict_class(annotation):
        # isinstance() rejects TypedDicts; check keys and values instead (#283)
        return _typed_dict_predicate(annotation)
    if annotation in (Any, object):
        return always_true_p  # every value is an object
    if type(annotation) is TypeVar:
        return _type_var_predicate(annotation)
    if annotation in (Never, NoReturn):
        return always_false_p  # no value inhabits Never
    if annotation is LiteralString:
        return is_str_p  # literal-ness is not observable at runtime
    if annotation is float:
        return is_instance_p(float, int)  # PEP 484 numeric tower: int is acceptable for float
    if annotation is complex:
        return is_instance_p(complex, float, int)
    if (io_predicate := _io_predicate(annotation)) is not None:
        return io_predicate
    origin = get_origin(annotation)
    if origin in _type_narrowing_origins:
        return always_true_p  # TypeGuard/TypeIs is bool at runtime
    if origin in _union_origins:
        return reduce(or_p, [annotation_to_predicate(t) for t in get_args(annotation)])
    if origin is Literal:
        return in_p(get_args(annotation))
    if origin is type and (args := get_args(annotation)):
        # A subclass of X; for a TypeVar its bound or constraints (binding T to other arguments is #258)
        return is_instance_p(type) & type_arg_predicate(args[0])
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


def _validate_args(f: Callable, spec: Spec) -> dict[str, Predicate]:
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

    parameters = _validate_args(f, spec)

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
            if key not in parameters:
                parameters[key] = exercise_param_predicate(parameter)
            else:
                if not implies(parameters[key], param_predicate(parameter)):
                    raise InvalidSpecError("Spec predicate is not a constrained annotation")

    return spec


def exercise_param_predicate(param: Parameter) -> Predicate:
    """Return the predicate exercise generates arguments from, when the spec doesn't name the parameter.

    A plain **kwargs gets no keywords: it's almost always forwarded to a callee with a fixed set of keywords, so random
    names only make the callee fail (#306). Name it in the spec to generate keywords. **kwargs: Unpack[TD] keeps its
    keywords, since TD lists them.
    """
    if param.kind == Parameter.VAR_KEYWORD and get_origin(param.annotation) is not Unpack:
        return eq_p({})  # yields {} forever; is_dict_p & is_empty_p would run out after one
    return param_predicate(param)


def param_predicate(param: Parameter) -> Predicate:
    if param.kind == Parameter.VAR_KEYWORD and get_origin(param.annotation) is Unpack:
        # **kwargs: Unpack[TD] (PEP 692): the kwargs dict itself must match TD, not each of its values (#343)
        return annotation_to_predicate(first(get_args(param.annotation)))
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


def is_unannotated_var_param(parameter: Parameter) -> bool:
    # Unannotated *args / **kwargs get no values: call_args then passes () and {}
    return parameter.annotation is parameter.empty and parameter.kind in (
        Parameter.VAR_POSITIONAL,
        Parameter.VAR_KEYWORD,
    )


def is_private_default_param(parameter: Parameter) -> bool:
    # `_re: Pattern = re.compile(...)`: an underscore plus a default means "don't pass this"; the default is used
    return parameter.name.startswith("_") and parameter.default is not parameter.empty


def is_skipped_param(parameter: Parameter) -> bool:
    """Parameters exercise generates no values for, so call_args leaves them out."""
    return is_unannotated_var_param(parameter) or is_private_default_param(parameter)


def no_spec_error(name: str, missing: str) -> InvalidSpecError:
    return InvalidSpecError(f"Cannot derive spec for '{name}': {missing}; pass a Spec or annotate it")

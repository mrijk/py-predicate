import types
import typing
from collections.abc import Iterator
from dataclasses import dataclass
from inspect import Parameter, signature
from typing import Callable, override

from predicate.predicate import Predicate


def get_union_args(cls) -> tuple | None:
    origin = typing.get_origin(cls)
    if origin is typing.Union or (hasattr(types, "UnionType") and origin is types.UnionType):
        return typing.get_args(cls)
    return None


def is_subclass_safe(cls, superclass) -> bool:
    # A "-> None" annotation is stored as None, not as NoneType
    cls = type(None) if cls is None else cls
    superclass = type(None) if superclass is None else superclass

    cls_union = get_union_args(cls)
    if cls_union is not None:
        # If the child is a Union, ALL types in the union must inherit from the superclass
        return all(is_subclass_safe(c, superclass) for c in cls_union)

    super_union = get_union_args(superclass)
    if super_union is not None:
        return any(is_subclass_safe(cls, s) for s in super_union)

    if not isinstance(cls, type) or not hasattr(cls, "__mro__"):
        return False

    return superclass in cls.__mro__


def remove_default_args(f_parameters, g_parameters):
    return types.MappingProxyType(
        {name: p for name, p in g_parameters.items() if name in f_parameters or p.default is Parameter.empty}
    )


@dataclass
class SameSignaturePredicate[T](Predicate[T]):
    """A predicate class that models the 'same signature as predicate."""

    function: Callable
    strict: bool

    def __call__(self, function: type) -> bool:
        return not any(self._failures(function))

    def _failures(self, function: type) -> Iterator[str]:
        f_sig = signature(self.function)
        g_sig = signature(function)

        # Check return type is covariant
        f_return = f_sig.return_annotation
        g_return = g_sig.return_annotation
        if not is_subclass_safe(g_return, f_return):
            yield f"Return type {g_return} is not a subtype of {f_return}"
            return

        # Check parameters
        f_parameters = f_sig.parameters
        g_parameters = remove_default_args(f_parameters, g_sig.parameters)

        # Leave out default parameters in g if they are not part of f

        if len(f_parameters) != len(g_parameters):
            yield f"Expected {len(f_parameters)} parameter(s), got {len(g_parameters)}"
            return

        for f_param, g_param in zip(f_parameters.items(), g_parameters.items(), strict=False):
            f_param_name, f_param_annotation = f_param
            g_param_name, g_param_annotation = g_param
            if f_param_name != g_param_name:
                yield f"Expected parameter '{f_param_name}', got '{g_param_name}'"
                return
            # Parameter types are contravariant
            if not is_subclass_safe(f_param_annotation.annotation, g_param_annotation.annotation):
                yield f"Parameter '{g_param_name}' has incompatible type"
                return

    @override
    def explain_failure(self, function: type) -> dict:
        return {"reason": next(self._failures(function))}


def same_signature_p(function: Callable, strict: bool = False) -> Predicate:
    """Return True if value has the same signature, otherwise False."""
    return SameSignaturePredicate(function=function, strict=strict)

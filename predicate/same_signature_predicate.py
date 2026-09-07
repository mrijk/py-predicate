import types
import typing
from dataclasses import dataclass
from inspect import signature
from typing import Callable

from predicate.predicate import Predicate


def get_union_args(cls) -> tuple | None:
    origin = typing.get_origin(cls)
    if origin is typing.Union or (hasattr(types, "UnionType") and origin is types.UnionType):
        return typing.get_args(cls)
    return None


def is_subclass_safe(cls, superclass) -> bool:
    super_union = get_union_args(superclass)
    if super_union is not None:
        return any(is_subclass_safe(cls, s) for s in super_union)

    cls_union = get_union_args(cls)
    if cls_union is not None:
        # Als de child een Union is, moeten ÁLLE types in de union overerven van de superclass
        return all(is_subclass_safe(c, superclass) for c in cls_union)

    if not isinstance(cls, type) or not hasattr(cls, "__mro__"):
        return False

    return superclass in cls.__mro__


def remove_default_args(f_parameters, g_parameters):
    return types.MappingProxyType({name: p for name, p in g_parameters.items() if name not in f_parameters})


@dataclass
class SameSignaturePredicate[T](Predicate[T]):
    """A predicate class that models the 'same signature as predicate."""

    function: Callable
    strict: bool

    def __call__(self, function: type) -> bool:
        f_sig = signature(self.function)
        g_sig = signature(function)

        # Check return type is covariant

        if not is_subclass_safe(g_sig.return_annotation, f_sig.return_annotation):
            return False

        # Check parameters
        f_parameters = f_sig.parameters
        g_parameters = remove_default_args(f_parameters, g_sig.parameters)

        # Leave out default parameters in g if they are not part of f

        if len(f_parameters) != len(g_parameters):
            return False

        for f_param, g_param in zip(f_parameters.items(), g_parameters.items(), strict=False):
            f_param_name, f_param_annotation = f_param
            g_param_name, g_param_annotation = g_param
            if f_param_name != g_param_name:
                return False
            if is_subclass_safe(f_param_annotation.annotation, g_param_annotation):
                return False

        return True


def same_signature_p(function: Callable, strict: bool = False) -> Predicate:
    """Return True if value has the same signature, otherwise False."""
    return SameSignaturePredicate(function=function, strict=strict)

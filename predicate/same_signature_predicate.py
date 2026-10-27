from collections.abc import Mapping
from dataclasses import dataclass
from inspect import Parameter, signature
from types import NoneType, UnionType
from typing import Any, Callable, Union, get_args, get_origin, override

from predicate.is_subclass_predicate import is_subclass_p
from predicate.predicate import Predicate


def is_subtype(cls: Any, superclass: Any) -> bool:
    # Any is compatible with every type, in both directions. A missing annotation counts as Any
    if any(t is Any or t is Parameter.empty for t in (cls, superclass)):
        return True
    # A "-> None" annotation is stored as None, not as NoneType
    return is_subclass_p(erase_generic(NoneType if superclass is None else superclass))(erase_generic(cls))


def erase_generic(t: Any) -> Any:
    # ponytail: type arguments are ignored, so list[str] matches list[int]; compare get_args if that matters
    if get_origin(t) in (Union, UnionType):
        return Union[tuple(erase_generic(arg) for arg in get_args(t))]
    return get_origin(t) or t


def remove_default_args(
    f_parameters: Mapping[str, Parameter], g_parameters: Mapping[str, Parameter]
) -> Mapping[str, Parameter]:
    # Extra parameters in g are fine when they're optional: a default, *args or **kwargs
    optional = (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD)
    # Positional parameters are matched by position, the others by name
    positional = (Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD)
    nr_positional = sum(p.kind in positional for p in f_parameters.values())
    return {
        name: p
        for i, (name, p) in enumerate(g_parameters.items())
        if (p.kind in positional and i < nr_positional)
        or name in f_parameters
        or (p.default is Parameter.empty and p.kind not in optional)
    }


def ordered(parameters: Mapping[str, Parameter]) -> list[tuple[str, Parameter]]:
    # Keyword-only parameters can be given in any order, so compare them by name
    return sorted(
        parameters.items(), key=lambda item: (item[1].kind, item[0] if item[1].kind == Parameter.KEYWORD_ONLY else "")
    )


@dataclass
class SameSignaturePredicate[T](Predicate[T]):
    """A predicate class that models the 'same signature as predicate."""

    function: Callable
    strict: bool

    def __call__(self, function: type) -> bool:
        return self._failure(function) is None

    def _failure(self, function: type) -> str | None:
        if not callable(function):
            return f"{function} is not callable"

        f_sig = signature(self.function, eval_str=True)
        try:
            g_sig = signature(function, eval_str=True)
        except ValueError:
            # Some builtins, like max, have no signature that can be inspected
            return f"{function} has no signature"

        # Check return type is covariant
        f_return = f_sig.return_annotation
        g_return = g_sig.return_annotation
        if not is_subtype(g_return, f_return):
            return f"Return type {g_return} is not a subtype of {f_return}"

        # Check parameters
        f_parameters = f_sig.parameters
        g_parameters = remove_default_args(f_parameters, g_sig.parameters)

        # Leave out default parameters in g if they are not part of f

        if len(f_parameters) != len(g_parameters):
            return f"Expected {len(f_parameters)} parameter(s), got {len(g_parameters)}"

        for f_param, g_param in zip(ordered(f_parameters), ordered(g_parameters), strict=False):
            f_param_name, f_param_annotation = f_param
            g_param_name, g_param_annotation = g_param
            # Callers of f can't pass a positional-only parameter by name, so its name doesn't matter
            if f_param_annotation.kind != Parameter.POSITIONAL_ONLY and f_param_name != g_param_name:
                return f"Expected parameter '{f_param_name}', got '{g_param_name}'"
            # Callers of f may pass this parameter by position or by name, so g must accept both
            f_kind, g_kind = f_param_annotation.kind, g_param_annotation.kind
            if f_kind == Parameter.POSITIONAL_OR_KEYWORD and g_kind != Parameter.POSITIONAL_OR_KEYWORD:
                return f"Parameter '{g_param_name}' is {g_kind.description}, expected {f_kind.description}"
            # Callers of f may leave out a parameter with a default, so g needs a default too
            if f_param_annotation.default is not Parameter.empty and g_param_annotation.default is Parameter.empty:
                return f"Parameter '{g_param_name}' has no default value"
            # Parameter types are contravariant
            if not is_subtype(f_param_annotation.annotation, g_param_annotation.annotation):
                return (
                    f"Parameter '{g_param_name}' has type {g_param_annotation.annotation}, "
                    f"expected {f_param_annotation.annotation}"
                )

        return None

    def __repr__(self) -> str:
        return f"same_signature_p({self.function.__name__})"

    @override
    def explain_failure(self, function: type) -> dict:
        return {"reason": self._failure(function)}


def same_signature_p(function: Callable, strict: bool = False) -> Predicate:
    """Return True if value has the same signature, otherwise False."""
    return SameSignaturePredicate(function=function, strict=strict)

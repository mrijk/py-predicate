from fnmatch import fnmatch
from inspect import isfunction
from typing import Any

from predicate.spec.instrument_function import OnError, default_on_error, instrument_function, is_instrumented
from predicate.spec.spec import Spec

_EMPTY_SPEC: Spec = {"args": {}}


def _get_descriptor(member: Any) -> type | None:
    return type(member) if isinstance(member, (staticmethod, classmethod)) else None


def instrument_class(cls: type, pattern: str | None = None, on_error: OnError = default_on_error) -> None:
    for name, member in list(vars(cls).items()):
        descriptor = _get_descriptor(member)
        func = member.__func__ if descriptor else member
        if isfunction(func) and not is_instrumented(func) and (pattern is None or fnmatch(name, pattern)):
            wrapped = instrument_function(func, _EMPTY_SPEC, on_error)
            setattr(cls, name, descriptor(wrapped) if descriptor else wrapped)

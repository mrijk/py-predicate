from dataclasses import dataclass
from typing import Any, Callable, override

from predicate.predicate import Explanation, Predicate
from predicate.spec.spec import InvalidSpecError, Spec


@dataclass
class IsValidSpecPredicate(Predicate[Spec]):
    """A predicate class that models the 'is valid spec for function' predicate."""

    function: Callable[..., Any]

    @override
    def __call__(self, spec: Spec) -> bool:
        return self._failure(spec) is None

    def _failure(self, spec: Spec) -> str | None:
        from predicate.spec.exercise_helpers import check_signature_against_spec

        try:
            check_signature_against_spec(self.function, spec)
        except InvalidSpecError as e:
            return str(e)
        return None

    def _name(self) -> str:
        from predicate.spec.exercise_helpers import callable_name

        return callable_name(self.function)

    @override
    def __repr__(self) -> str:
        return f"is_valid_spec_p({self._name()})"

    @override
    def _explain(self, x: Spec, *args: Any, **kwargs: Any) -> Explanation:
        if (reason := self._failure(x)) is None:
            return {"result": True}
        return {"result": False, "reason": reason}

    @override
    def explain_failure(self, spec: Spec) -> Explanation:
        return {"reason": self._failure(spec)}


def is_valid_spec_p(function: Callable[..., Any]) -> IsValidSpecPredicate:
    """Return True if the spec is valid for the function, otherwise False."""
    return IsValidSpecPredicate(function=function)

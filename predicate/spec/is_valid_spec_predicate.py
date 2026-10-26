from dataclasses import dataclass
from typing import Callable, override

from predicate.predicate import Predicate
from predicate.spec.exercise_helpers import check_signature_against_spec
from predicate.spec.spec import InvalidSpecError, Spec


@dataclass
class IsValidSpecPredicate(Predicate[Spec]):
    """A predicate class that models the 'is valid spec for function' predicate."""

    function: Callable

    def __call__(self, spec: Spec) -> bool:
        return self._failure(spec) is None

    def _failure(self, spec: Spec) -> str | None:
        try:
            check_signature_against_spec(self.function, spec)
        except InvalidSpecError as e:
            return str(e)
        return None

    def __repr__(self) -> str:
        return f"is_valid_spec_p({self.function.__name__})"

    @override
    def explain_failure(self, spec: Spec) -> dict:
        return {"reason": self._failure(spec)}


def is_valid_spec_p(function: Callable) -> Predicate[Spec]:
    """Return True if the spec is valid for the function, otherwise False."""
    return IsValidSpecPredicate(function=function)

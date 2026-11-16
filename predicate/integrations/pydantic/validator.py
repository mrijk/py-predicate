from dataclasses import dataclass
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import PydanticCustomError, core_schema

from predicate.predicate import Predicate


@dataclass(frozen=True)
class PredicateValidator:
    """Pydantic metadata: `Annotated[int, PredicateValidator(ge_p(0) & lt_p(100))]`.

    Runs after the inner type's own validation.
    """

    predicate: Predicate[Any]

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        def validate(value: Any) -> Any:
            if self.predicate(value):
                return value
            try:
                explanation = self.predicate.explain_failure(value)
            except NotImplementedError:  # ponytail: predicates without explain_failure get no detail
                explanation = {}
            raise PydanticCustomError(
                "predicate_failed",
                "Predicate failed: {predicate}",
                {"predicate": repr(self.predicate), "explanation": explanation},
            )

        return core_schema.no_info_after_validator_function(validate, handler(source_type))

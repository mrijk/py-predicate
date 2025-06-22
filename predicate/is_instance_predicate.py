from collections.abc import Callable, Container, Iterable
from dataclasses import dataclass
from datetime import datetime
from typing import Hashable, Iterator, override
from uuid import UUID

from predicate.helpers import join_with_or
from predicate.predicate import Predicate


@dataclass
class IsInstancePredicate[T](Predicate[T]):
    """A predicate class that models the 'isinstance' predicate."""

    instance_klass: type | tuple

    def __call__(self, x: object) -> bool:
        # This is different from standard Python behaviour: a False/True value is not an int!
        if isinstance(x, bool) and self.instance_klass[0] is int:  # type: ignore
            return False
        return isinstance(x, self.instance_klass)

    def __repr__(self) -> str:
        name = self.instance_klass[0].__name__  # type: ignore
        return f"is_{name}_p"

    @override
    def get_klass(self) -> type:
        return self.instance_klass  # type: ignore

    @override
    def explain_failure(self, x: T) -> dict:
        def class_names() -> Iterator[str]:
            match self.instance_klass:
                case tuple() as klasses:
                    for klass in klasses:
                        yield klass.__name__
                case _:
                    yield self.instance_klass.__name__

        klasses = join_with_or(list(class_names()))

        return {"reason": f"{x} is not an instance of type {klasses}"}


def is_instance_p(*klass: type) -> Predicate:
    """Return True if value is an instance of one of the classes, otherwise False."""
    return IsInstancePredicate(instance_klass=klass)


is_bool_p = is_instance_p(bool)
"""Returns True if the value is a bool, otherwise False."""

is_bytearray_p = is_instance_p(bytearray)
"""Returns True if the value is a bytearray, otherwise False."""

is_callable_p = is_instance_p(Callable)  # type: ignore
"""Returns True if the value is a callable, otherwise False."""

is_complex_p = is_instance_p(complex)
"""Returns True if the value is a complex, otherwise False."""

is_container_p = is_instance_p(Container)
"""Returns True if the value is a container (list, set, tuple, etc.), otherwise False."""

is_datetime_p = is_instance_p(datetime)
"""Returns True if the value is a datetime, otherwise False."""

is_dict_p = is_instance_p(dict)
"""Returns True if the value is a dict, otherwise False."""

is_float_p = is_instance_p(float)
"""Returns True if the value is a float, otherwise False."""

is_hashable_p = is_instance_p(Hashable)
"""Returns True if the value is hashable, otherwise False."""

is_iterable_p = is_instance_p(Iterable)
"""Returns True if the value is an Iterable, otherwise False."""

is_int_p = is_instance_p(int)
"""Returns True if the value is an integer, otherwise False."""

is_list_p = is_instance_p(list)
"""Returns True if the value is a list, otherwise False."""

is_predicate_p = is_instance_p(Predicate)
"""Returns True if the value is a predicate, otherwise False."""

is_range_p = is_instance_p(range)
"""Returns True if the value is a range, otherwise False."""

is_set_p = is_instance_p(set)
"""Returns True if the value is a set, otherwise False."""

is_str_p = is_instance_p(str)
"""Returns True if the value is a str, otherwise False."""

is_tuple_p = is_instance_p(tuple)
"""Returns True if the value is a tuple, otherwise False."""

is_uuid_p = is_instance_p(UUID)
"""Returns True if the value is a UUID, otherwise False."""

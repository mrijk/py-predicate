beartype
--------

`beartype <https://github.com/beartype/beartype>`_ accepts any callable as a validator through
``beartype.vale.Is``. Since predicates are callables, they can be used directly in type hints, no wrapper needed:

.. code-block:: python

    from typing import Annotated

    from beartype import beartype
    from beartype.vale import Is

    from predicate import ge_p, is_list_of_p, is_str_p, lt_p

    Percentage = Annotated[int, Is[ge_p(0) & lt_p(101)]]


    @beartype
    def set_volume(level: Percentage) -> Percentage:
        return level


    @beartype
    def join(words: Annotated[list, Is[is_list_of_p(is_str_p)]]) -> str:
        return " ".join(words)


    set_volume(50)  # ok
    set_volume(101)  # raises BeartypeCallHintParamViolation
    join(["a", 1])  # raises BeartypeCallHintParamViolation

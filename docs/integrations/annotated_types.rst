annotated-types
---------------

`annotated-types <https://github.com/annotated-types/annotated-types>`_ provides ``Predicate``, which takes any
callable returning a ``bool``. Predicates can be used directly, no wrapper needed. annotated-types itself doesn't
validate anything; a library like `pydantic <https://docs.pydantic.dev/>`_ enforces the constraint:

.. code-block:: python

    from typing import Annotated

    from annotated_types import Predicate
    from pydantic import BaseModel

    from predicate import ge_lt_p, is_str_p

    class Person(BaseModel):
        name: Annotated[str, Predicate(is_str_p)]
        age: Annotated[int, Predicate(ge_lt_p(0, 150))]

    Person(name="alice", age=30)  # ok
    Person(name="alice", age=200)  # raises ValidationError

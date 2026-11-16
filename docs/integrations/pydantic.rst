Pydantic
--------

`Pydantic <https://docs.pydantic.dev>`_ (v2) fields can be validated with a predicate. Install the optional
dependency first:

.. code-block:: bash

    pip install py_predicate[pydantic]

``PredicateValidator`` is importable from ``predicate.pydantic``, which is a short alias for
``predicate.integrations.pydantic``. Use it as ``Annotated`` metadata. It runs *after* the validation of the
inner type:

.. code-block:: python

    from typing import Annotated

    from pydantic import BaseModel

    from predicate import ge_p, lt_p
    from predicate.pydantic import PredicateValidator


    class Model(BaseModel):
        x: Annotated[int, PredicateValidator(ge_p(0) & lt_p(100))]


    Model(x=5)  # ok
    Model(x=100)  # ValidationError

A failing predicate raises a ``predicate_failed`` error. Its context holds the predicate (``predicate``) and the
result of ``explain_failure`` (``explanation``), available through ``ValidationError.errors()``.

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

JSON Schema
^^^^^^^^^^^

The constraints also show up in the generated JSON Schema (and so in OpenAPI and FastAPI docs):

.. code-block:: python

    TypeAdapter(Annotated[int, PredicateValidator(ge_p(0) & lt_p(100))]).json_schema()
    # {'type': 'integer', 'minimum': 0, 'exclusiveMaximum': 100}

``predicate_to_json_schema`` does the mapping and can be used on its own:

======================================  ====================================================================
Predicate                               JSON Schema
======================================  ====================================================================
``ge_p``, ``gt_p``, ``le_p``, ``lt_p``  ``minimum``, ``exclusiveMinimum``, ``maximum``, ``exclusiveMaximum``
``eq_p``, ``in_p``                      ``const``, ``enum``
``&``                                   merge the keywords (``allOf`` if a keyword is used twice)
``|``                                   ``anyOf``
``~``                                   ``not``
``all_p``, ``any_p``                    ``items``, ``contains``
``regex_p``                             ``pattern`` (anchored at the start, like ``re.match``)
======================================  ====================================================================

Predicates without a mapping are left out of the schema, but are still enforced at validation time. In ``a | b`` and
``~a`` an unmapped operand drops the whole expression, since a partial schema would reject valid values.

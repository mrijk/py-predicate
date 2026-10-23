pandera
-------

`pandera <https://pandera.readthedocs.io/>`_ accepts any callable as a check through ``pandera.Check``.
With ``element_wise=True`` the check is called per value, so predicates can be used directly, no wrapper needed:

.. code-block:: python

    import pandas as pd
    import pandera.pandas as pa

    from predicate import ge_lt_p, is_str_p

    schema = pa.DataFrameSchema(
        {
            "name": pa.Column(checks=pa.Check(is_str_p, element_wise=True)),
            "age": pa.Column(int, pa.Check(ge_lt_p(0, 150), element_wise=True)),
        }
    )

    schema.validate(pd.DataFrame({"name": ["alice"], "age": [30]}))  # ok
    schema.validate(pd.DataFrame({"name": ["alice"], "age": [200]}))  # raises SchemaError

import pandas as pd
import pandera.pandas as pa
import pytest
from pandera.errors import SchemaError

from predicate import ge_lt_p, is_str_p

schema = pa.DataFrameSchema(
    {
        "name": pa.Column(checks=pa.Check(is_str_p, element_wise=True)),
        "age": pa.Column(int, pa.Check(ge_lt_p(0, 150), element_wise=True)),
    }
)


def test_pandera_valid():
    df = pd.DataFrame({"name": ["alice", "bob"], "age": [30, 40]})

    assert schema.validate(df).equals(df)


def test_pandera_invalid():
    df = pd.DataFrame({"name": ["alice", "bob"], "age": [30, 200]})

    with pytest.raises(SchemaError):
        schema.validate(df)


def test_pandera_invalid_type():
    df = pd.DataFrame({"name": ["alice", 1], "age": [30, 40]})

    with pytest.raises(SchemaError):
        schema.validate(df)

import pytest

from predicate import explain


def test_explain_nested():
    pass  # TODO


def test_explain_not_implemented(unknown_p):
    with pytest.raises(NotImplementedError):
        explain(unknown_p, None)

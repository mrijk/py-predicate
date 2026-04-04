import pytest

from predicate import explain


@pytest.mark.skip
def test_explain_nested():
    pass  # TODO


@pytest.mark.skip
def test_explain_not_implemented(unknown_p):
    with pytest.raises(NotImplementedError):
        explain(unknown_p, None)

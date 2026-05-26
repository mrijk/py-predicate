import pytest

from predicate import eq_p
from predicate.accepts_predicate import accepts_p


@pytest.mark.parametrize(
    "predicate, accepted_types, rejected_types",
    [
        # (eq_p(2), (int, ), (bool, str)),
        # (eq_p("foo"), (str, ), (bool, int)),
        # (eq_p(3.14), (float, ), (str, int, bool)),
        (
            eq_p(2) | eq_p("foo"),
            (
                int,
                str,
            ),
            (bool,),
        )
    ],
)
def test_accepts(predicate, accepted_types, rejected_types):
    accepts = accepts_p(predicate=predicate)

    for accepted in accepted_types:
        assert accepts(accepted)

    for rejected in rejected_types:
        assert not accepts(rejected)

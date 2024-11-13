from predicate import regex_p


def test_regex_predicate():
    predicate = regex_p("^foo.*bar$")

    assert not predicate("foo")
    assert not predicate("foobarr")
    assert not predicate(" foobar ")

    assert predicate("foobar")
    assert predicate("foooooobar")

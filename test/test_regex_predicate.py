from predicate import explain, regex_p


def test_regex_predicate():
    predicate = regex_p("^foo.*bar$")

    assert not predicate("foo")
    assert not predicate("foobarr")
    assert not predicate(" foobar ")

    assert predicate("foobar")
    assert predicate("foooooobar")


def test_regex_p_explain():
    predicate = regex_p("^foo.*bar$")

    expected = {"result": False, "reason": "String foo didn't match patter ^foo.*bar$"}
    assert explain(predicate, "foo") == expected

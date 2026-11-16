import predicate


def test_all_names_exist():
    assert [name for name in predicate.__all__ if not hasattr(predicate, name)] == []

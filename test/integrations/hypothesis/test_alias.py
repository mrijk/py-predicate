import predicate.hypothesis as short
import predicate.integrations.hypothesis as full


def test_short_import_path_exposes_the_same_objects():
    assert short.__all__ == full.__all__
    assert all(getattr(short, name) is getattr(full, name) for name in full.__all__)


def test_real_hypothesis_is_not_shadowed():
    import hypothesis

    assert hypothesis.__file__ and "site-packages" in hypothesis.__file__

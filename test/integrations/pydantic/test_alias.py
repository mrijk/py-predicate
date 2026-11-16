import predicate.integrations.pydantic as full
import predicate.pydantic as short


def test_short_import_path_exposes_the_same_objects():
    assert short.__all__ == full.__all__
    assert all(getattr(short, name) is getattr(full, name) for name in full.__all__)


def test_real_pydantic_is_not_shadowed():
    import pydantic

    assert pydantic.__file__ and "site-packages" in pydantic.__file__

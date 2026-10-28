from fractions import Fraction

from more_itertools import take

from predicate.spec.exercise import exercise
from predicate.spec.exercise_helpers import resolved_signature
from predicate.spec.type_checking import type_checking_namespace
from spec.test_functions import sample_module
from spec.test_functions.type_checking_names import first, ratio


def test_type_checking_namespace():
    namespace = type_checking_namespace(ratio)

    assert namespace["Fraction"] is Fraction
    assert namespace["collections"].abc.Sequence  # `import a.b` binds `a`
    assert namespace["sample_module"] is sample_module  # relative import


def test_type_checking_namespace_without_block():
    assert type_checking_namespace(sample_module.add) == {}


def test_type_checking_namespace_builtin():
    assert type_checking_namespace(len) == {}


def test_resolved_signature_type_checking_name():
    sig = resolved_signature(ratio)

    assert sig.parameters["x"].annotation is Fraction


def test_exercise_type_checking_name():
    assert take(3, exercise(first))


def test_type_checking_namespace_skips_calls(tmp_path, monkeypatch):
    (tmp_path / "with_call.py").write_text(
        "from typing import TYPE_CHECKING\n"
        "if TYPE_CHECKING:\n"
        "    Alias = int | None\n"
        "    Called = print('side effect')\n"
        "def f(x: 'Alias') -> int:\n"
        "    return 0\n"
    )
    monkeypatch.syspath_prepend(tmp_path)
    import with_call  # type: ignore[import-not-found]  # noqa: PLC0415

    namespace = type_checking_namespace(with_call.f)

    assert namespace == {"Alias": int | None}


def test_type_checking_namespace_skips_missing_name(tmp_path, monkeypatch):
    package = tmp_path / "pkg327"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / "types_.py").write_text(
        "from typing import TYPE_CHECKING\nNumber = int | float\nif TYPE_CHECKING:\n    Sorter = int\n"
    )
    (package / "use.py").write_text(
        "from typing import TYPE_CHECKING\n"
        "if TYPE_CHECKING:\n"
        "    from pkg327.types_ import Sorter, Number\n"
        "def f(x: 'Number') -> int:\n"
        "    return 0\n"
    )
    monkeypatch.syspath_prepend(tmp_path)
    from pkg327 import use  # type: ignore[import-not-found]  # noqa: PLC0415

    assert type_checking_namespace(use.f) == {"Number": int | float}

import warnings
from collections.abc import Callable
from fractions import Fraction
from typing import Any

import pytest
from more_itertools import take

from predicate.spec.exercise import exercise
from predicate.spec.exercise_helpers import resolved_signature
from predicate.spec.spec import UnresolvedAnnotationWarning
from predicate.spec.type_checking import type_checking_namespace
from spec.test_functions import sample_module
from spec.test_functions.runtime_unsubscriptable import is_dispatch_method, misspelt
from spec.test_functions.type_checking_names import first, ratio
from spec.test_functions.type_checking_only_classes import bound, bound_type, config_name, pair_first


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


def test_type_checking_namespace_rewritten_module(monkeypatch):
    monkeypatch.setattr(ratio, "__module__", "spec")

    assert type_checking_namespace(ratio)["Fraction"] is Fraction


def test_resolved_signature_alias_from_other_module(tmp_path, monkeypatch):
    package = tmp_path / "pkg333"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / "types_.py").write_text(
        "from typing import TYPE_CHECKING, Union\n"
        "if TYPE_CHECKING:\n"
        "    from fractions import Fraction\n"
        "Number = Union[int, 'Fraction']\n"
    )
    (package / "use.py").write_text("from pkg333.types_ import Number\ndef f(x: Number) -> int:\n    return 0\n")
    monkeypatch.syspath_prepend(tmp_path)
    from pkg333 import use  # type: ignore[import-not-found]  # noqa: PLC0415

    assert type_checking_namespace(use.f) == {}
    assert resolved_signature(use.f).parameters["x"].annotation == int | Fraction


def test_resolved_signature_alias_with_runtime_name_from_other_module(tmp_path, monkeypatch):
    package = tmp_path / "pkg333b"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / "types_.py").write_text("from typing import Any, Union\nItems = Union[int, 'list[Any]']\n")
    (package / "use.py").write_text("from pkg333b.types_ import Items\ndef f(x: Items) -> int:\n    return 0\n")
    monkeypatch.syspath_prepend(tmp_path)
    from pkg333b import use  # type: ignore[import-not-found]  # noqa: PLC0415

    assert resolved_signature(use.f).parameters["x"].annotation == int | list[Any]


def test_resolved_signature_alias_does_not_shadow_builtins(tmp_path, monkeypatch):
    package = tmp_path / "pkg333c"
    package.mkdir()
    (package / "__init__.py").write_text("def list(): ...\n")
    (package / "types_.py").write_text(
        "from typing import Union\nNumber = Union[int, 'Fraction']\nfrom fractions import Fraction\n"
    )
    (package / "use.py").write_text(
        "from __future__ import annotations\n"
        "from pkg333c import list as _list\n"
        "from pkg333c.types_ import Number\n"
        "def f(x: Number, y: list[int]) -> int:\n"
        "    return 0\n"
    )
    monkeypatch.syspath_prepend(tmp_path)
    from pkg333c import use  # type: ignore[import-not-found]  # noqa: PLC0415

    parameters = resolved_signature(use.f).parameters
    assert parameters["y"].annotation == list[int]


def test_type_checking_namespace_type_vars(tmp_path, monkeypatch):
    (tmp_path / "with_type_vars.py").write_text(
        "import typing\n"
        "from collections.abc import Callable\n"
        "from typing import TYPE_CHECKING, Any, TypeVar\n"
        "if TYPE_CHECKING:\n"
        "    F = TypeVar('F', bound=Callable[..., Any])\n"
        "    N = typing.TypeVar('N', int, float)\n"
        "    Called = TypeVar(print('side effect'))\n"
        "    Bound = TypeVar('Bound', bound=print('side effect'))\n"
        "def f(x: 'F') -> 'N':\n"
        "    return 0\n"
    )
    monkeypatch.syspath_prepend(tmp_path)
    import with_type_vars  # type: ignore[import-not-found]  # noqa: PLC0415

    namespace = type_checking_namespace(with_type_vars.f)

    assert set(namespace) == {"F", "N"}
    assert namespace["F"].__bound__ == Callable[..., Any]
    assert namespace["N"].__constraints__ == (int, float)


def test_resolved_signature_runtime_unsubscriptable():
    with pytest.warns(UnresolvedAnnotationWarning, match="'return' in is_dispatch_method"):
        sig = resolved_signature(is_dispatch_method)

    assert sig.return_annotation is Any
    assert sig.parameters["obj"].annotation is Any


def test_exercise_unresolvable_annotation_is_any():
    with pytest.warns(UnresolvedAnnotationWarning, match="'x' in misspelt"):
        sig = resolved_signature(misspelt)
        values = list(exercise(misspelt, n=3))

    assert sig.parameters["x"].annotation is Any
    assert sig.parameters["y"].annotation is int
    assert len(values) == 3


def test_unresolvable_annotation_warning_can_be_an_error():
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnresolvedAnnotationWarning)
        with pytest.raises(UnresolvedAnnotationWarning):
            resolved_signature(misspelt)


@pytest.mark.parametrize(
    "f, message",
    [
        (bound, "'Hidden' in the bound of TypeVar HiddenT"),
        (bound_type, "'Hidden' in the bound of TypeVar HiddenT"),
        (config_name, "field 'hidden' in Config"),
        (pair_first, "field 'hidden' in Pair"),
    ],
)
def test_exercise_type_checking_only_class_is_any(f, message):
    with pytest.warns(UnresolvedAnnotationWarning, match=message):
        values = list(exercise(f, n=3))

    assert len(values) == 3

import importlib.util
import inspect
import sys
from collections.abc import Iterator
from pathlib import Path
from types import ModuleType
from typing import Any

from predicate.is_pure_predicate import find_impurity


def _load(file: Path) -> ModuleType:
    # ponytail: loads by file location, so modules using relative imports end up as errors; add package-aware import if needed
    name = f"_purity_{abs(hash(file.resolve()))}"
    spec = importlib.util.spec_from_file_location(name, file)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {file}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        del sys.modules[name]
        raise
    return module


def _public_functions(module: ModuleType) -> Iterator[tuple[str, Any]]:
    names = getattr(module, "__all__", None)
    return (
        (name, fn)
        for name, fn in inspect.getmembers(module, inspect.isfunction)
        if (name in names if names is not None else not name.startswith("_")) and fn.__module__ == module.__name__
    )


def _function_entry(name: str, fn: Any) -> dict[str, Any]:
    impurity = find_impurity(fn)
    entry = {"name": name, "line": fn.__code__.co_firstlineno, "pure": impurity is None}
    return entry if impurity is None else entry | {"category": impurity.category, "reason": impurity.reason}


def _analyze_file(file: Path) -> dict[str, Any]:
    try:
        module = _load(file)
    except BaseException as e:  # noqa: BLE001 - importing user code can fail in any way
        return {"path": str(file), "file_name": file.name, "error": f"{type(e).__name__}: {e}", "functions": []}
    functions = [_function_entry(name, fn) for name, fn in _public_functions(module)]
    return {"path": str(file), "file_name": file.name, "functions": sorted(functions, key=lambda f: f["line"])}


def analyze(path: Path) -> list[dict[str, Any]]:
    """Report the purity of all public module-level functions found under path. Imports (executes) the modules."""
    files = [path] if path.is_file() else sorted(path.rglob("*.py"))
    return [_analyze_file(file) for file in files]


def summarize(modules: list[dict[str, Any]]) -> dict[str, int]:
    functions = [f for m in modules for f in m["functions"]]
    pure = sum(f["pure"] for f in functions)
    return {"total": len(functions), "pure": pure, "impure": len(functions) - pure}

import ast
import inspect
import textwrap
from typing import Callable


def get_fn_source(fn: Callable) -> dict[str, str]:
    """Return serializable info about fn's source."""
    try:
        source_file = inspect.getfile(fn)
    except (OSError, TypeError):
        return _builtin_info(fn)

    if fn.__name__ != "<lambda>":
        try:
            raw = inspect.getsource(fn)
            return {"source": textwrap.dedent(raw).strip()}
        except OSError:
            return _builtin_info(fn)

    # Lambda: parse full file, find Lambda node on the right line
    try:
        with open(source_file) as f:
            tree = ast.parse(f.read())
    except (OSError, SyntaxError):
        return {}

    target_line = fn.__code__.co_firstlineno
    candidates = [n for n in ast.walk(tree) if isinstance(n, ast.Lambda) and n.lineno == target_line]

    if not candidates:
        return {}
    if len(candidates) == 1:
        chosen = candidates[0]
    else:
        body_col = _get_body_col(fn)
        exact = [n for n in candidates if body_col is not None and n.body.col_offset == body_col]
        chosen = exact[0] if exact else candidates[0]

    return {"source": ast.unparse(chosen)}


def _builtin_info(fn: Callable) -> dict[str, str]:
    name = getattr(fn, "__qualname__", getattr(fn, "__name__", str(fn)))
    module = getattr(fn, "__module__", None)
    qualname = f"{module}.{name}" if module else name
    return {"qualname": qualname}


def _get_body_col(fn: Callable) -> int | None:
    try:
        cols = [col for _, _, col, _ in fn.__code__.co_positions() if col]
        return cols[0] if cols else None
    except AttributeError:
        return None

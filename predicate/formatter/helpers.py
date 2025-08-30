from typing import Iterable


def set_to_str(v: Iterable) -> str:
    items = ", ".join(str(item) for item in v)
    return f"{{{items}}}"

# With `from __future__ import annotations`, TypedDict can't see NotRequired[...] in its string annotations
from __future__ import annotations

from typing import NotRequired, TypedDict


class Options(TypedDict):
    name: str
    verbose: NotRequired[bool]

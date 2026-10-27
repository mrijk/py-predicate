# No `from __future__ import annotations`: on Python 3.14+ annotations are evaluated lazily (PEP 649),
# so Node can only be resolved once the class body has finished
from predicate.spec.instrument import instrument


class Node:
    @instrument
    def child(self, other: Node) -> Node:  # noqa: F821 (only valid on 3.14+, see above)
        return other

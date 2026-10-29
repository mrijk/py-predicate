from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.or_predicate import OrPredicate


class FreeTypeVarPredicate(AlwaysTruePredicate):
    """always_true_p for a free type variable T, whose generated values all have one type (#375).

    It equals always_true_p, so checking is unchanged; only generation differs.
    """

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AlwaysTruePredicate)


class ConstrainedTypeVarPredicate(OrPredicate):
    """c1 | c2 for TypeVar("T", c1, c2), whose generated values all fit one of the constraints (#375).

    It equals the plain OrPredicate, so checking is unchanged; only generation differs.
    """

    def __eq__(self, other: object) -> bool:
        return isinstance(other, OrPredicate) and (self.left, self.right) == (other.left, other.right)

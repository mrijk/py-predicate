from predicate import (
    AllPredicate,
    XorPredicate,
    AndPredicate,
    EqPredicate,
    OrPredicate,
    NotPredicate,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
)
from predicate.standard_predicates import is_instance_p

is_all_p = is_instance_p(AllPredicate)
is_and_p = is_instance_p(AndPredicate)
is_not_p = is_instance_p(NotPredicate)
is_or_p = is_instance_p(OrPredicate)
is_xor_p = is_instance_p(XorPredicate)
is_false_p = is_instance_p(AlwaysFalsePredicate)
is_true_p = is_instance_p(AlwaysTruePredicate)
is_eq_p = is_instance_p(EqPredicate)

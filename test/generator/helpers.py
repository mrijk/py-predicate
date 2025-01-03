from predicate import is_bool_p, is_datetime_p, is_float_p, is_int_p, is_str_p


def combinations_of_2():
    predicates = [is_bool_p, is_float_p, is_int_p, is_str_p, is_datetime_p]
    for predicate_1 in predicates:
        for predicate_2 in predicates:
            if predicate_1 != predicate_2:
                yield predicate_1, predicate_2

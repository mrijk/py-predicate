# CHANGELOG.md

## 1.5.0 (unreleased)

Features:

- new juxt_p that handles juxtaposition of predicates
- new type check predicates: is_bytes_p, is_date_p, is_frozenset_p, is_mapping_p, is_number_p, is_path_p, is_sequence_p, is_time_p, is_timedelta_p
- async support for exercise
- generator support for is_hashable_p
- implies-based optimization in xor_optimizer
- optimize le_p & le_p and lt_p & lt_p in and_optimizer

Bugfixes:

- fix exercise for predicates with generic Iterable annotation
- fix DeprecationWarning for _UnionGenericAlias in generate_is_subclass
- fix mixed types handling in class_from_set and add size guard in InPredicate.__eq__
- report which path step failed in has_path_p explain_failure
- include function name in comp_p repr
- fix imports of is_bool_p, is_dict_p, is_list_p, zero_p from __init__

## 1.4.0

Features:

- new convenience predicates none_is_false_p, none_is_exception and none_is_true_p to handle None values
- new is_p to handle 'is' comparisons
- new recur_p to create recursive predicates
- new mutual_recur_p to create mutual recursive predicates
- match_p now also accepts predicates that act on iterables

## 1.3.0

Features:

- in_p predicate now works for all container classes (list, dict, tuple, range, etc)
- is_subclass_p to test if a class is a subclass of another class
- is_enum_p, is_int_enum_p and is_str_enum_p as special predicates of is_subclass_p
- count_p to test if an iterable has a number (also a predicate) of elements that satisfy a predicate
- improved LaTeX formatting

Breaking changes:

- in_p used to convert its parameters to a set. Now it only accepts a container class.

## 1.2.0

Features:

- Implementation of exercise
- Many improvements to implies_p
- First implementation of instrument for run-time checking functions against predicates

## 1.1.0

Features:

- Values for generators that create iterables, can now be restricted with a predicate
- Explain message for is_instance_p (for example is_int_p, is_str_p, etc.) has been improved
- Added generators for is_even_p and is_odd_p
- generate_false for has_length_p now generates different lengths

Breaking changes:
- None

Bugfixes:
- is_set_of now only accepts sets

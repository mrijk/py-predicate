# CHANGELOG.md

## 1.3.0 (unreleased)

Features:

- in_p predicate now works for all container classes (list, dict, tuple, range, etc)
- is_subclass_p to test if a class is a subclass of another class
- is_enum_p, is_int_enum_p and is_str_enum_p as special predicates of is_subclass_p

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

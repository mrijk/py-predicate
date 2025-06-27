# CHANGELOG.md

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

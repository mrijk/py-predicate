Tutorial 3: using match_p
=========================

The match_p was introduced with version 0.9 of py-predicate. It's a regular expression
implementation with a twist: instead of using a regex on a string, you can use
regular expressions with predicates, applied to any iterable. A few examples will make
this more clear.

A minimal example
-----------------

In this example we introduce the ``match_p`` predicate.

We will define a matcher that matches an iterable on an ``int``, followed by a ``str``:

.. code-block:: python

    from predicate import match_p, is_int_p, is_str_p

    predicate = match_p(is_int_p, is_str_p)

    predicate([2])  # False
    predicate([1, "foo"])  # True

``match_p`` accepts all the predicates (including ``match_p`` itself!) defined in py-predicate,
and applies them one by one to the Iterable.

This is convenient, but the real power of his approach can be seen once we start using regex operators.

The ``optional`` operator
-------------------------

This is an implementation of the ? (question mark) that indicates that either 0 or 1 matches of the
predicate should evaluate to True.

In this example we want to match a list that should start with zero or one integers, followed by a string:

.. code-block:: python

    from predicate import match_p, is_int_p, is_str_p, optional

    maybe_int = optional(is_int_p)
    predicate = match_p(maybe_int, is_str_p)

    predicate([2])  # False
    predicate(["foo"])  # True
    predicate([1, "foo"])  # True
    predicate([1, 2, "foo"])  # False

The ``star`` operator
---------------------

This is an implementation of the * (asterisk) that indicates that either 0 or more matches of the
predicate should evaluate to True.

In this example we want to match a list that should start with zero or more integers, followed by a string:

.. code-block:: python

    from predicate import match_p, is_int_p, is_str_p, star

    zero_or_more_ints = star(is_int_p)
    predicate = match_p(zero_or_more_ints, is_str_p)

    predicate([2])  # False
    predicate(["foo"])  # True
    predicate([1, "foo"])  # True
    predicate([1, 2, "foo"])  # True


The ``plus`` operator
---------------------

This is an implementation of the + (polus) that indicates that either 1 or more matches of the
predicate should evaluate to True.

In the following example we want to match on at least one integer, followed by at least one string:

.. code-block:: python

    from predicate import match_p, is_int_p, is_str_p, plus

    one_or_more_ints = plus(is_int_p)
    one_or_more_strings = plus(is_str_p)

    predicate = match_p(one_or_more_ints, one_or_more_ints)

    predicate([2])  # False
    predicate(["foo"])  # False
    predicate([1, "foo"])  # True
    predicate([1, 2, "foo"])  # True


The ``repeat`` operator
-----------------------

Sometimes you want to check for a range. In standard regular syntax this is indicated with curly brackets.

In the following example we match on an iterable starting with 2 or 3 integers, followed by a string:

.. code-block:: python

    from predicate import match_p, is_int_p, is_str_p, repeat

    one_or_two_ints = repeat(2, 3, is_int_p)

    predicate = match_p(one_or_two_ints, is_str_p)

    predicate([1])  # False
    predicate([1, "foo"])  # False
    predicate([1, 2, "foo"])  # True
    predicate([1, 2, 3, 4, "foo"])  # False

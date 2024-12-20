Tutorial 1
~~~~~~~~~~

Task: define a predicate expression that given a list of values, returns True if:

#. all values are either strings or integers
#. if the value is an integer, than it should be less than 5
#. if the value is a string, it should start with foo

This will show a couple of concepts and useful standard predicates.

Let's start with the first requirement. We start first with the code and then explain it:

.. code-block:: python

    from predicate import all_p, is_int_p, is_str_p

    predicate = all_p(is_int_p | is_str_p)


In the example above we import 3 predicates. The ``all_p`` accepts one parameter, which is another predicate. The
``is_int_p`` checks if a value is an integer. And finally the ``is_str_p`` checks if a value is a string.

We combine the ``is_int_p`` and ``is_str_p`` with the ``|`` operator, resulting in a new predicate.

This is sufficient for the first requirement. Now lets restrict the allowed value of the integer to less than 5:

.. code-block:: python

    from predicate import all_p, is_int_p, is_str_p, lt_p

    is_int_lt_5 = is_int_p & lt_p(5)

    predicate = all_p(is_int_lt_5 | is_str_p)

As you can see, we imported the ``lt_p`` predicate. This checks if a given value, is less than the parameter
(5 in this case). We could have made this a one-liner, but we assigned it to a new predicate variable
``is_int_lt_5``. With this addition, we have implemented the second requirement.

Finally we turn to the third requirement, which says that if the value is a string, it should start with "foo".
This sounds like an ideal candidate for a regular expression, and indeed such a predicate is also available:

.. code-block:: python

    from predicate import all_p, is_int_p, is_str_p, lt_p, regex_p

    is_int_lt_5 = is_int_p & lt_p(5)
    is_str_foo = is_str_p & regex_p("^foo.*")

    predicate = all_p(is_int_lt_5 | is_str_foo)

Now you are ready to check your new predicate against the requirements, for example:

.. code-block:: python

    predicate([1, "foo"])  # True
    predicate([1, "foo", None])  # False, None is not valid
    predicate([5, "foo"])  # False, 5 is to big
    predicate([1, "bar"])  # False, "bar" doesn't begin with "foo"

Let's now reuse this predicate to generate some sample values:

.. code-block:: python

    from predicate import generate_true
    from more_itertools import take

    result = take(10, generate_true(predicate))

Notice that this may take a few seconds. On my system the output was:

.. code-block:: python

    [
        [],
        (1, -1, "foo", "foo!", "foo!", 'foo"'),
        {0, -5, "foo"},
        ["foo5xT", "foo5xT", "foo", "foo ", "foo!", -1],
        (0, -1, -1, -1, "foo"),
        {"fooU7", "fooRV8TMtF", "foor959aO5"},
        [-9, "foo", "foojBA", "foo ", "foo "],
        ("foohqhdJr", "foou", "foo", 1, 1, 1, 1, 1, 2),
        {1, "foo", "foo!", -1, 'foo"'},
        ["foo", -1, -1, "foo", "foo", "foo ", 0, 'foo"', 'foo"'],
    ]

If you don't want to check manually if these values are correct, you can of course use a predicate:

.. code-block:: python

    validate = all_p(predicate)
    validate(result)

This should result in ``True``. If not, please submit a bug report.

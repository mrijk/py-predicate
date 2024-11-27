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
    is_str_foo = is_str_p & regex_p("^foo")

    predicate = all_p(is_int_lt_5 | is_str_foo)

Now you are ready to check your new predicate against the requirements, for example:

.. code-block:: python

    predicate([1, "foo"])  # True
    predicate([1, "foo", None])  # False, None is not valid
    predicate([5, "foo"])  # False, 5 is to big
    predicate([1, "bar"])  # False, "bar" doesn't begin with "foo"

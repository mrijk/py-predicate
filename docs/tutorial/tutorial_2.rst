Tutorial 2
~~~~~~~~~~

Task: define a predicate expression that given a list of values, returns True if:

#. any value is a tuple
#. the first element of that tuple is a uuid
#. the second element of that tuple is in the set {"foo", "bar"}
#. the third element of that tuple is a truthy value (True, 1, etc.)

Let's start with the first requirement. This is similar to what we saw in tutorial 1:

.. code-block:: python

    from predicate import any_p, is_tuple_p

    predicate = any_p(is_tuple_p)

The ``any_p`` predicate is similar to the ``all_p`` predicate: it accepts one parameter (which is a predicate) and
returns true iff at least one value satisfies this predicate.

Now lets turn to the other requirements. If it's a tuple, we need to check the elements in this tuple against three
different predicates. This is exactly what ``is_tuple_of_p`` does for us. Lets show the code first:

.. code-block:: python

    from predicate import any_p, in_p, is_truthy_p, is_tuple_of_p, is_uuid_p

    foo_or_bar = in_p("foo", "bar")
    valid_tuple = is_tuple_of_p(is_uuid_p, foo_or_bar, is_truthy_p)

    predicate = any_p(valid_tuple)

Now you are ready to check your new predicate against the requirements, for example:

.. code-block:: python

    from uuid import uuid4

    predicate([(uuid4(), "foo", 1)])  # True: 1 is a truthy value
    predicate([(uuid4(), "meh", 1)])  # False: missing "foo" or "bar"
    predicate([("not_a_uuid", "foo", 1)])  # False: missing uuid

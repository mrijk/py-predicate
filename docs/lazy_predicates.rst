Lazy predicates
===============

Lazy predicates are a more advanced feature that allow composing predicates that reference
themself, or even having predicates with mutual references.

A lazy predicate is defined as:

.. code-block:: python

    from predicate import lazy_p

    p = lazy_p("name_of_referenced_predicate")

To make this more clear, we will give to examples.

Example 1
---------
In the next example we define a predicate, that tests if a given data structure is
either a string, or a list of data that can again either be a string or a list of
data. Ad infinitum.

.. code-block:: python

    from predicate import all_p, is_list_p, is_str_p, lazy_p

    str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str")))

Note that the name of the reference must be the same as the variable name of the predicate that you are
referencing.

Applying this predicate gives the following results:

.. code-block:: python

    str_or_list_of_str("foo")
    True

    str_or_list_of_str(["foo"])
    True

    str_or_list_of_str(["foo", ["bar"]])
    True

    str_or_list_of_str(1)
    False

Example 2
---------
We can even model a predicate that checks if a given data structure is valid json:

.. code-block:: python

    valid_json_p = lazy_p("is_json_p")
    json_list_p = is_list_p & lazy_p("valid_values")

    json_keys_p = all_p(is_str_p)

    valid_values = all_p(
        is_str_p | is_int_p | is_float_p | json_list_p | valid_json_p | is_none_p
    )
    json_values_p = comp_p(lambda x: x.values(), valid_values)

    is_json_p = (is_dict_p & json_keys_p & json_values_p) | json_list_p

As you can see in this example there are 2 mutual lazy references.

this_p
------

A this predicate (this_p) is defined as:

.. code-block:: python

    from predicate import this_p

    p = this_p

Note that this example is not very useful, since it references itself, leading to an infinite recursion while
trying to evaluate.

For a more realist example, lets write example 1 from ``lazy_p`` using the ``this_p``:

Example 1
~~~~~~~~~

.. code-block:: python

    from predicate import is_list_of_p, is_str_p, this_p

    str_or_list_of_str = is_str_p | is_list_of_p(this_p)

We made two changes to the original lazy_p example. Firstly, are using the ``is_list_of_p`` predicate that combines the
``is_list`` and ``all_p`` predicates. But most importantly, instead of having to reference the ``str_or_list_of_str``
by name, we just use ``this_p``, leading to more concise code.

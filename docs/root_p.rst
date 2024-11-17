root_p
------

A this predicate (root_p) is defined as:

.. code-block:: python

    from predicate import root_p

    p = root_p

Note that this example is not very useful, since it references itself, leading to an infinite recursion while
trying to evaluate.

For a more realist example, lets write example 1 from ``lazy_p`` using the ``root_p``:

Example 1
~~~~~~~~~

.. code-block:: python

    from predicate import is_list_of_p, is_str_p, root_p

    str_or_list_of_str = is_str_p | is_list_of_p(root_p)

We made two changes to the original lazy_p example. Firstly, are using the ``is_list_of_p`` predicate that combines the
``is_list`` and ``all_p`` predicates. But most importantly, instead of having to reference the ``str_or_list_of_str``
by name, we just use ``root_p``, leading to more concise code.

Also note that in this particular case there is not difference between the ``this_p`` and the ``root_p``

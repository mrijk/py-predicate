Formatters
==========

Predicates can be formatted either as json or Graphviz dot files.

Json
----
Outputting a predicate as a json structure makes it easy to use tools such as
`jq <https://jqlang.github.io/jq/>`_ to inspect the layout.

.. code-block:: python

    from predicate import to_json, ne_p

    predicate = ne_p(13)

    json = to_json(predicate)

    assert json == {"ne": {"v": 13}}

Dotty
-----
Predicates can also be rendered in a visual way, using `Graphviz <https://graphviz.org/>`_

.. code-block:: python

    from predicate import ne_p, to_dot

    predicate = ne_p(13)

    dot = to_dot(predicate, "title")

    dot.render("/tmp/predicate.gv", view=True)

In sample above, we render a simple predicate.

CLI
===

py-predicate comes with a CLI that makes it easy to generate for example truth tables from the
commandline.

To show the available options:

.. code-block:: sh

    python main.py --help

Truth table
-----------

To generate a truth table:

.. code-block:: sh

    python main.py table "p & q"

This will output:

.. code-block:: txt

    p q
    0 0:   0
    0 1:   0
    1 0:   0
    1 1:   1


JSON output
-----------

For example (assuming you have `jq <https://jqlang.github.io/jq/>`_ installed):

.. code-block:: sh

    python main.py table "p & ~q" | jq.

will output:

.. code-block:: json

    {
      "and": {
        "left": {
          "variable": "p"
        },
        "right": {
          "not": {
            "predicate": {
              "variable": "q"
            }
          }
        }
      }
    }

Note: this format might change in future versions of py-predicate

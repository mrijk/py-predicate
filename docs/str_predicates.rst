String predicates
-----------------

A collection of predicates that act on strings.

ends_with_p
~~~~~~~~~~~

Return True if the string ends with the given suffix, otherwise False.

.. code-block:: python

    from predicate import ends_with_p

    ends_with_ing = ends_with_p("ing")

    assert ends_with_ing("running")
    assert not ends_with_ing("run")

is_alnum_p
~~~~~~~~~~

Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_alnum_p

    assert is_alnum_p("abc123")
    assert not is_alnum_p("abc 123")
    assert not is_alnum_p("")

is_alpha_p
~~~~~~~~~~

Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_alpha_p

    assert is_alpha_p("abc")
    assert not is_alpha_p("abc123")

is_ascii_p
~~~~~~~~~~

Return True if the string is empty or all characters in the string are ASCII, False otherwise.

.. code-block:: python

    from predicate import is_ascii_p

    assert is_ascii_p("hello")
    assert is_ascii_p("")
    assert not is_ascii_p("héllo")

is_decimal_p
~~~~~~~~~~~~

Return True if all characters in the string are decimal characters and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_decimal_p

    assert is_decimal_p("123")
    assert not is_decimal_p("12.3")
    assert not is_decimal_p("")

is_digit_p
~~~~~~~~~~

Return True if all characters in the string are digits and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_digit_p

    assert is_digit_p("123")
    assert not is_digit_p("12.3")

is_identifier_p
~~~~~~~~~~~~~~~

Return True if the string is a valid Python identifier, False otherwise.

.. code-block:: python

    from predicate import is_identifier_p

    assert is_identifier_p("my_var")
    assert is_identifier_p("_private")
    assert not is_identifier_p("123abc")
    assert not is_identifier_p("my-var")

is_lower_p
~~~~~~~~~~

Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise.

.. code-block:: python

    from predicate import is_lower_p

    assert is_lower_p("hello")
    assert not is_lower_p("Hello")

is_numeric_p
~~~~~~~~~~~~

Return True if all characters in the string are numeric characters and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_numeric_p

    assert is_numeric_p("123")
    assert not is_numeric_p("12.3")

is_printable_p
~~~~~~~~~~~~~~

Return True if all characters in the string are printable or the string is empty, False otherwise.

.. code-block:: python

    from predicate import is_printable_p

    assert is_printable_p("hello")
    assert is_printable_p("")
    assert not is_printable_p("hello\x00")

is_space_p
~~~~~~~~~~

Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_space_p

    assert is_space_p("   ")
    assert is_space_p("\t\n")
    assert not is_space_p("")
    assert not is_space_p("hello")

is_title_p
~~~~~~~~~~

Return True if the string is titlecased (each word starts with an uppercase letter) and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_title_p

    assert is_title_p("Hello World")
    assert not is_title_p("hello world")
    assert not is_title_p("HELLO WORLD")

is_upper_p
~~~~~~~~~~

Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.

.. code-block:: python

    from predicate import is_upper_p

    assert is_upper_p("HELLO")
    assert not is_upper_p("Hello")

starts_with_p
~~~~~~~~~~~~~

Return True if the string starts with the given prefix, otherwise False.

.. code-block:: python

    from predicate import starts_with_p

    starts_with_py = starts_with_p("py")

    assert starts_with_py("python")
    assert not starts_with_py("java")

String predicates
-----------------

A collection of predicates that act on strings.

contains_p
~~~~~~~~~~

Use ``contains_p`` for case-sensitive substring matching in a string.
An empty substring matches every string, so there are no non-matching examples to generate.

.. code-block:: python

    from predicate import contains_p

    contains_apple = contains_p("apple")

    assert contains_apple("a green apple")
    assert not contains_apple("a green pear")

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

is_blank_p
~~~~~~~~~~

Return True if the string is empty or only contains whitespace, False otherwise.

.. code-block:: python

    from predicate import is_blank_p

    assert is_blank_p("")
    assert is_blank_p(" \t\n")
    assert not is_blank_p(" a ")

is_camel_case_p
~~~~~~~~~~~~~~~

Return True if the string is camelCase (starts lowercase, no separators), False otherwise.

.. code-block:: python

    from predicate import is_camel_case_p

    assert is_camel_case_p("fooBar")
    assert not is_camel_case_p("FooBar")
    assert not is_camel_case_p("foo_bar")

is_capitalized_p
~~~~~~~~~~~~~~~~

Return True if the first character is uppercase and the rest is lowercase, False otherwise. Unlike ``is_title_p``, only the first word counts.

.. code-block:: python

    from predicate import is_capitalized_p

    assert is_capitalized_p("Hello world")
    assert not is_capitalized_p("Hello World")
    assert not is_capitalized_p("hello")

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

is_int_str_p
~~~~~~~~~~~~

Return True for strings (including subclasses) accepted by Python's ``int(value)``
with its default base of 10. Non-string values return False without conversion.
Signs, surrounding whitespace accepted by ``int``, underscores between digits,
and Unicode decimal digits are supported. Empty strings, decimal points,
exponents and base prefixes are rejected. Python's active integer-string length
limit applies; a conversion rejected by that limit returns False. No whitespace
preprocessing or global limit changes are performed.

.. code-block:: python

    from predicate import is_int_str_p

    assert is_int_str_p("0")
    assert is_int_str_p("-5")
    assert is_int_str_p(" 1_000 ")
    assert not is_int_str_p("1.0")
    assert not is_int_str_p(5)

Both true and false string generators are provided.

is_kebab_case_p
~~~~~~~~~~~~~~~

Return True if the string is kebab-case, False otherwise.

.. code-block:: python

    from predicate import is_kebab_case_p

    assert is_kebab_case_p("foo-bar")
    assert not is_kebab_case_p("foo_bar")
    assert not is_kebab_case_p("Foo-bar")

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

is_regex_p
~~~~~~~~~~

Return True if the value is a string that compiles as a valid regular expression, False otherwise.

.. code-block:: python

    from predicate import is_regex_p

    assert is_regex_p(r"^\d{3}$")
    assert is_regex_p("")
    assert not is_regex_p("(")
    assert not is_regex_p(42)

is_single_line_p
~~~~~~~~~~~~~~~~

Return True if the string contains no newline, False otherwise.

.. code-block:: python

    from predicate import is_single_line_p

    assert is_single_line_p("hello world")
    assert not is_single_line_p("hello\nworld")

is_snake_case_p
~~~~~~~~~~~~~~~

Return True if the string is snake_case, False otherwise.

.. code-block:: python

    from predicate import is_snake_case_p

    assert is_snake_case_p("foo_bar")
    assert not is_snake_case_p("foo-bar")
    assert not is_snake_case_p("Foo_bar")

is_space_p
~~~~~~~~~~

Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.

.. code-block:: python

    from predicate import is_space_p

    assert is_space_p("   ")
    assert is_space_p("\t\n")
    assert not is_space_p("")
    assert not is_space_p("hello")

is_stripped_p
~~~~~~~~~~~~~

Return True if the string has no leading or trailing whitespace, False otherwise.

.. code-block:: python

    from predicate import is_stripped_p

    assert is_stripped_p("hello world")
    assert not is_stripped_p(" hello")
    assert not is_stripped_p("hello\n")

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

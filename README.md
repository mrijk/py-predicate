Small Python library to create composable predicates

# Example

```python
    filtered = [x for x in range(10) if x >= 2 and x <= 3]
```

Version with predicates:

```python
    ge_2 = ge_p(2)
    le_3 = le_p(3)

    between_2_and_3 = ge_2 & le_3
    filtered = [x for x in range(10) if between_2_and_3(x)]
```

Of course this example looks way more complicated than the original version. The point here is that you can build
reusable predicates that can be used in multiple locations
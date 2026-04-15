from predicate import explain
from predicate.is_async_predicate import is_async_p


def test_is_async_with_async_function():
    async def async_fn():
        pass

    assert is_async_p(async_fn)


def test_is_async_with_regular_function():
    def sync_fn():
        pass

    assert not is_async_p(sync_fn)


def test_is_async_with_lambda():
    assert not is_async_p(lambda: None)


def test_is_async_with_non_callable():
    assert not is_async_p(42)


def test_is_async_explain():
    def sync_fn():
        pass

    expected = {"reason": f"{sync_fn} is not an async function", "result": False}
    assert explain(is_async_p, sync_fn) == expected


def test_is_async_repr():
    assert repr(is_async_p) == "is_async_p"

import sys
from functools import wraps
from typing import Callable

from predicate import explain
from predicate.spec.spec import Spec


def instrument_function(func: Callable, spec: Spec) -> Callable:
    func_name = func.__name__

    @wraps(func)
    def wrapped(*args, **kwargs):
        from inspect import signature

        bound = signature(func).bind(*args, **kwargs)
        bound.apply_defaults()

        result = func(*args, **kwargs)

        parameters = spec["args"]
        for name, predicate in parameters.items():
            if name in bound.arguments:
                value = bound.arguments[name]
                if not predicate(value):
                    reason = explain(predicate, value)["reason"]
                    raise ValueError(f"Parameter predicate for function {func_name} failed. Reason: {reason}")

        return_p = spec["ret"]
        if not return_p(result):
            reason = explain(return_p, result)["reason"]
            raise ValueError(f"Return predicate for function {func_name} failed. Reason: {reason}")

        return result

    # Attach metadata
    wrapped.__spec__ = spec  # type: ignore

    module_name = func.__module__
    module = sys.modules.get(module_name)

    if module and hasattr(module, func_name):
        setattr(module, func_name, wrapped)
    else:
        pass
        # print(f"[instrument_function] WARNING: Could not find {module_name}.{func_name} to patch.")

    return wrapped

import sys
from functools import wraps
from typing import Callable

from predicate import explain
from predicate.spec.spec import Spec


def instrument_function(func: Callable, spec: Spec) -> Callable:
    func_name = func.__name__

    @wraps(func)
    def wrapped(*args, **kwargs):
        # spec.check_inputs(args, kwargs, func)
        result = func(*args, **kwargs)

        return_p = spec["ret"]
        if not return_p(result):
            reason = explain(return_p, result)["reason"]
            raise ValueError(f"Return predicate for function {func_name} failed. Reason: {reason}")

        return result

    # Attach metadata
    wrapped.__spec__ = spec

    module_name = func.__module__
    module = sys.modules.get(module_name)

    if module and hasattr(module, func_name):
        setattr(module, func_name, wrapped)
    else:
        pass
        # print(f"[instrument_function] WARNING: Could not find {module_name}.{func_name} to patch.")

    return wrapped

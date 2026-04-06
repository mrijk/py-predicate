import sys
from functools import wraps
from inspect import signature, unwrap
from typing import Callable

from predicate import explain
from predicate.spec.spec import Spec


def instrument_function(func: Callable, spec: Spec) -> Callable:
    func = unwrap(func)
    func_name = func.__name__

    @wraps(func)
    def wrapped(*args, **kwargs):
        bound = signature(func).bind(*args, **kwargs)
        bound.apply_defaults()

        for name, predicate in spec["args"].items():
            if name in bound.arguments:
                value = bound.arguments[name]
                if not predicate(value):
                    reason = explain(predicate, value)["reason"]
                    raise ValueError(f"Parameter predicate for function {func_name} failed. Reason: {reason}")

        result = func(*args, **kwargs)

        if return_p := spec.get("ret"):
            if not return_p(result):
                reason = explain(return_p, result)["reason"]
                raise ValueError(f"Return predicate for function {func_name} failed. Reason: {reason}")

        if fn := spec.get("fn"):
            if not fn(**bound.arguments, ret=result):
                raise ValueError(f"fn constraint for function {func_name} failed.")

        if fn_p := spec.get("fn_p"):
            p = fn_p(**bound.arguments)
            if not p(result):
                reason = explain(p, result)["reason"]
                raise ValueError(f"fn_p constraint for function {func_name} failed. Reason: {reason}")

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

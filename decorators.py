from functools import wraps
from exceptions import InvalidAmountError
import inspect
from functools import wraps


def validate_amount( field="amount"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = inspect.signature(func).bind(*args, **kwargs)
            bound.apply_defaults()

            try:
                value = float(bound.arguments[field])
            except (ValueError, TypeError):
                raise InvalidAmountError("Amount must be a valid number.")

            if value <= 0:
                raise InvalidAmountError("Amount must be greater than 0.")

            bound.arguments[field] = value
            return func(*bound.args, **bound.kwargs)

        return wrapper

    return decorator
from functools import wraps


def validate_title(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        title = args[1]

        if not title.strip():
            raise ValueError("Title cannot be empty")

        return func(*args, **kwargs)

    return wrapper

from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def inner(*args):
            try:
                return int(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner

    @staticmethod
    def to_str(func):
        @wraps(func)
        def inner(*args):
            try:
                return str(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def inner(*args):
            try:
                return bool(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner

    @staticmethod
    def to_float(func):
        @wraps(func)
        def inner(*args):
            try:
                return float(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_int
def adds(a, b):
    return a + b


@TypeDecorators.to_float
def adds(a, b):
    return a + b


@TypeDecorators.to_str
def adds(a, b):
    return a + b


@TypeDecorators.to_bool
def adds(a, b):
    return a + b

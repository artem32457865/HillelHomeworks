def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def positive_only(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("усі позиційні аргументи повинні бути додатними числами")
        return func(*args, **kwargs)
    return wrapper


@positive_only
def add_two(x):
    return x + 2


@shout
def add_suffix(value):
    return value + "suffix"



print(add_two(5))

print(add_suffix("i"))
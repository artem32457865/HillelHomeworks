def log_args(func):
    def wrapper(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@log_args
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet("Artem", 18)
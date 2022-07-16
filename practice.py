import os
import functools


def decorator(func):
    @functools.wraps(func)
    def inner(*args):
        str1 = func(*args)
        return str1.upper()
    return inner


@decorator
def greet(name):
    return f"good morning {name}"


print(greet("James"))
import os


def upper(func):
    
    def wrapper():
        return func().upper()
    return wrapper


@upper
def greeting():
    name = "john"
    return f"hello {name}"


print(greeting())
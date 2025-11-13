# Class 11/13/25, introducing *args and **kwargs in decorators

def my_simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution.")
        result = func(*args, **kwargs)
        print("After function execution.")
        return result
    return wrapper

@my_simple_decorator
def greet():
    print("Hello, World!")

greet()

@my_simple_decorator
def add(a, b):
    print(f"The sum is: {a + b}")

add(3, 5)
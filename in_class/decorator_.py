# Class 11/13/25

import time

def my_decorator(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f"Execution time: {end - start} seconds")
    return wrapper

@my_decorator
def execution_time():
    total = 0
    n = 10_000_000
    for i in range(n):
        total += i
    return total

print(execution_time())

@my_decorator
def time_dictionaries():
    n = 100000
    total = 0
    d1 = {}
    for i in range(n):
        d1[i] = i
    for i in range(n):
        total += d1[i]
    return total

print(time_dictionaries())
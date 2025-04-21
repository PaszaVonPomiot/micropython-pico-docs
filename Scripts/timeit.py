"""
Decorators to measure the execution time of a function in milliseconds or microseconds.
"""

import time


def timeit_ms(func):
    def wrapper(*args, **kwargs):
        start = time.ticks_ms()
        result = func(*args, **kwargs)
        duration = time.ticks_diff(time.ticks_ms(), start)
        print(f"Function {func.__name__} took {duration} ms")
        return result

    return wrapper


def timeit_us(func):
    def wrapper(*args, **kwargs):
        start = time.ticks_us()
        result = func(*args, **kwargs)
        duration = time.ticks_diff(time.ticks_us(), start)
        print(f"Function {func.__name__} took {duration} us")
        return result

    return wrapper

import sys


def log_exception():
    try:
        a = [1] * (10**8)  # MemoryError
    except MemoryError as error:
        with open("error.log", "w") as file:
            sys.print_exception(error, file)


log_exception()

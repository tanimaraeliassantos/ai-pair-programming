from functools import lru_cache

FIVE_NAMES = ["Joe", "Jane", "John", "Jill", "Jack"]

AGES = [25, 30, 22, 28, 35]

MAP_NAME_TO_AGE = {name: age for name, age in zip(FIVE_NAMES, AGES)}


def average_age():
    return sum(AGES) / len(AGES)


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence


@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

LAST_NAMES = ["Smith", "Doe", "Brown", "Johnson", "Williams"]

def fib3(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)

    return fib_sequence

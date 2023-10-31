def sum_array(arg: list) -> int:
    total = 0
    for element in arg:
        total += element
    return total


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

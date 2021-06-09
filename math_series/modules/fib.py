# should return the nth value in the fib series
# recursive solution
def fibonacci_recursive(n):
    """
    Returns nth value in the fibonacci series recursively.

    0, 1, 1, 2, 3, 5, 8, 13, ..
    """
    # Base case:
    # Can't return negative numbers
    if n < 0:
        return "Incorrect Input"

    # Check if n is 0, then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2. It will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def lucas(n):
    """
    Returns nth value in the lucas numbers recursively.

    2, 1, 3, 4, 7, 11, 18, 29, ...
    """
    pass


def sum_series(n, num_one=0, num_two=1):
    """
    n determines which element in the series to print.

    Optional param's determine first two values for series
    """
    pass


def fib_recursive(n):
    """
    Returns nth value in the fibonacci series recursively.
    Fibonacci sequence begins with 0
    Example: 0, 1, 1, 2, 3, 5, 8, 13, ..
    """
    # BASE CASE:
    # Can't return negative numbers
    if n < 0:
        return "No negative numbers"
    # Check if n is 0, then it will return 0
    elif n == 0:
        return 0
    # Check if n is 1,2. It will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_refactor(n):
    if n <= 1:
        return n
    else:
        return(fib_refactor(n-1) + fib_refactor(n-2))


def dynamic_fib_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # list for tabulation
    table = [None] * (n + 1)
    # BASE CASE:
    table[0] = 0
    table[1] = 1
    # iteratively fills table starting from 2 -> n
    # end of iteration returns nth fib number at last index
    for tabulation in range(2, n + 1):
        table[tabulation] = table[tabulation - 1] + table[tabulation - 2]
    return table[n]


# Global so it's available to all dynamic_fib_top_down() calls
memoize_top_down = {}


def dynamic_fib_top_down(n):
    # BASE CASE:
    if n == 0:
        return 0
    if n == 1:
        return 1
    # check if already evaluated, if so, memoized value returned.
    # otherwise evaluate recursively
    elif n in memoize_top_down:
        return memoize_top_down[n]
    else:
        memoize_top_down[n] = dynamic_fib_top_down(n - 1) + dynamic_fib_top_down(n - 2)
        return memoize_top_down[n]

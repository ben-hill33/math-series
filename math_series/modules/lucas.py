
def lucas(n):
    """
    Returns nth value in the lucas numbers recursively.
    Lucas sequence begins with 2
    Example: 2, 1, 3, 4, 7, 11, 18, 29, ...
    """
    if n < 0:
        return "Incorrect Input"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return(lucas(n-1) + lucas(n-2))


def lucas_iter(n):
    """
    Returns nth value in lucas numbers iteratively

    O(n) time complexity
    """
    a = 2
    b = 1

    if n == 0:
        return a

    for num in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

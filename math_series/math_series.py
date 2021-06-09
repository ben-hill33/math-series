

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    if n <= 0:
        return "Incorrect Input"
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return(lucas(n-2) + lucas(n-1))


def sum_series(val, val_two):
    if val == 0 and val_two == 1:
        return (val, val_two)

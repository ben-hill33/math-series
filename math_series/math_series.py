

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return(fibonacci(n-1) + fibonacci(n-2))

def lucas(n):
  if n == 1:
    return n

def sum_series(val, val_two):
  if val == 0 and val_two == 1:
    return (val, val_two)


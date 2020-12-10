from math_series import __version__
from math_series.math_series import *
import pytest

def test_version():
    assert __version__ == '0.1.0'

# tested whether expected and actual 
# need to be 

def test_fib_life():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_lucas_life():
    expected = 2
    actual = lucas(1)
    assert actual == expected

def test_sum_series_life():
    expected = 0, 1
    actual = sum_series(0, 1)
    assert actual == expected

def test_fib_value():
    expected = 5
    actual = fibonacci(5)
    assert actual == expected

def test_lucas_value():
    expected = 18
    actual = lucas(7)
    assert actual == expected



from math_series.modules.fib import fibonacci_recursive


def test_no_negative_numbers():
    expected = "Incorrect Input"
    actual = fibonacci_recursive(-1)
    assert actual == expected


def test_zero_return_zero():
    expected = 0
    actual = fibonacci_recursive(0)
    assert actual == expected


def test_one_return_one():
    expected = 1
    actual = fibonacci_recursive(1)
    assert actual == expected


def test_two_return_one():
    expected = 1
    actual = fibonacci_recursive(2)
    assert actual == expected


def test_three_return_two():
    expected = 2
    actual = fibonacci_recursive(3)
    assert actual == expected

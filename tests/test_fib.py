from math_series.modules.fib import (
    fib_recursive,
    dynamic_fib_bottom_up,
    dynamic_fib_top_down
)


def test_no_negative_numbers():
    expected = "No negative numbers"
    actual = fib_recursive(-1)
    assert actual == expected


def test_zero_return_zero():
    expected = 0
    actual = fib_recursive(0)
    assert actual == expected


def test_one_return_one():
    expected = 1
    actual = fib_recursive(1)
    assert actual == expected


def test_two_return_one():
    expected = 1
    actual = fib_recursive(2)
    assert actual == expected


def test_three_return_two():
    expected = 2
    actual = fib_recursive(3)
    assert actual == expected


def test_10_return_55():
    expected = 55
    actual = fib_recursive(10)
    assert actual == expected


def test_dyn_bott_up_zero():
    expected = 0
    actual = dynamic_fib_bottom_up(0)
    assert actual == expected


def test_dyn_bott_up_10_return_55():
    expected = 55
    actual = fib_recursive(10)
    assert actual == expected


def test_top_down_zero():
    expected = 0
    actual = dynamic_fib_top_down(0)
    assert actual == expected


def test_top_down_10_return_55():
    expected = 55
    actual = fib_recursive(10)
    assert actual == expected

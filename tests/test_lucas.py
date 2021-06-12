from math_series.modules.lucas import (
    lucas,
    lucas_iter,
)


def test_zero_return_two():
    expected = 2
    actual = lucas(0)
    assert actual == expected


def test_one_return_one():
    expected = 1
    actual = lucas(1)
    assert actual == expected


def test_three_return_four():
    expected = 4
    actual = lucas(3)
    assert actual == expected


def test_four_return_seven():
    expected = 7
    actual = lucas(4)
    assert actual == expected


def test_five_return_eleven():
    expected = 11
    actual = lucas(5)
    assert actual == expected


def test_six_return_eighteen():
    expected = 18
    actual = lucas(6)
    assert actual == expected


def test_seven_return_twentynine():
    expected = 29
    actual = lucas(7)
    assert actual == expected


def test_eight_return_eleven():
    expected = 47
    actual = lucas(8)
    assert actual == expected


def test_iter_zero_return_two():
    expected = 2
    actual = lucas_iter(0)
    assert actual == expected


def test_iter_one_return_one():
    expected = 1
    actual = lucas_iter(1)
    assert actual == expected


def test_iter_three_return_four():
    expected = 4
    actual = lucas_iter(3)
    assert actual == expected


def test_iter_four_return_seven():
    expected = 7
    actual = lucas_iter(4)
    assert actual == expected


def test_iter_five_return_eleven():
    expected = 11
    actual = lucas_iter(5)
    assert actual == expected


def test_iter_six_return_eighteen():
    expected = 18
    actual = lucas_iter(6)
    assert actual == expected


def test_iter_seven_return_twentynine():
    expected = 29
    actual = lucas_iter(7)
    assert actual == expected


def test_iter_eight_return_eleven():
    expected = 47
    actual = lucas_iter(8)
    assert actual == expected

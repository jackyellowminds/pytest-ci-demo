import pytest

from calculator import add, subtract, multiply, divide


@pytest.mark.smoke
def test_add(numbers):
    a, b = numbers

    assert add(a, b) == 30


@pytest.mark.regression
def test_subtract(numbers):
    a, b = numbers

    assert subtract(b, a) == 10


@pytest.mark.regression
def test_multiply(numbers):
    a, b = numbers

    assert multiply(a, b) == 200


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 20, 30),
        (5, 5, 10),
        (100, 200, 300),
        (-5, 10, 5)
    ]
)
def test_add_multiple_cases(a, b, expected):
    assert add(a, b) == expected
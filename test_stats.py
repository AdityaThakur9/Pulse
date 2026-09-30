import pytest
from stats import average


def test_average_of_two_numbers():
    assert average([5, 15]) == 10.0


def test_average_of_three_numbers():
    assert average([4,5,6]) == 5.0


def test_average_of_empty_list():
    assert average([]) is None


def test_average_of_single_number():
    assert average([42]) == 42.0

def test_average_of_negative_numbers():
    assert average([-5, -15]) == -10.0

def test_average_of_decimal_numbers():
    assert average([0.1, 0.2]) == pytest.approx(0.15)
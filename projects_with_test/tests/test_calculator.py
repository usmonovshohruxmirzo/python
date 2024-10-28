import pytest
from ..calculator import add
from ..calculator import division
from ..calculator import multiplication
from ..calculator import subtraction

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_division_positive_numbers():
    result, message = division(10, 2)
    assert result == 5
    assert message == "The result of 10 divided by 2 is 5.0"

def test_division_zero_denominator():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        division(10, 0)

def test_multiplication():
    assert multiplication(5, 5) == 25

def test_subtraction():
    assert subtraction(10, 10) == 0
    assert subtraction(10, 5) == 5
    assert subtraction(-10, 2) == -12
    assert subtraction(0, 0) == 0


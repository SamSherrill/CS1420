# 10/23/25 class, beginning discussion on testing
# This file will test calulator_OOP.py

from calculator_OOP import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(0, 0) == 0

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(0, 0) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2
    assert calc.divide(-1, 1) == -1
    assert calc.divide(0, 1) == 0
    try:
        calc.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
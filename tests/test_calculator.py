"""
Automated unit tests for the calculator module using pytest.
"""
import pytest
from src.calculator import Calculator

def test_add():
    """Test the addition functionality."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    """Test the subtraction functionality."""
    calc = Calculator()
    assert calc.subtract(10, 5) == 5

def test_multiply():
    """Test the multiplication functionality."""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_divide():
    """Test the division functionality including edge cases."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    
    with pytest.raises(ValueError):
        calc.divide(10, 0)
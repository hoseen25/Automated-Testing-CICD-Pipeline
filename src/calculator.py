"""
Basic calculator module for the automated CI/CD pipeline project.
"""

class Calculator:
    """A class that performs basic arithmetic operations."""
    
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference between two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the division of two numbers. Raise ValueError on divide by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
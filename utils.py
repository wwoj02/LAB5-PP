"""Zestaw podstawowych funkcji kalkulatora."""


def add(a: int, b: int) -> int:
    """suma a i b"""
    return a + b


def subtract(a: int, b: int) -> int:
    """roznica a i b"""
    return a - b


def multiply(a: int, b: int) -> int:
    """iloczyn a i b"""
    return a * b


def divide(a: int, b: int) -> float:
    """iloraz a i b jesli b == 0 podnosi wyjatek"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

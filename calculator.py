"""Простой калькулятор для изучения CI/CD."""


def add(a, b):
    """Вернуть сумму двух чисел."""
    return a + b


def divide(a, b):
    """Вернуть результат деления a на b.

    При делении на ноль вызвать ValueError.
    """
    if b == 0:
        raise ValueError("Деление на ноль запрещено")
    return a / b


def multiply(a, b):
    """Вернуть произведение двух чисел."""
    return a * b
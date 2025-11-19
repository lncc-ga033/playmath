from __future__ import annotations

from collections.abc import Sequence


def add(a: float, b: float) -> float:
    """
    Soma dois números.

    Parameters
    ----------
    a : float
        Primeiro operando.
    b : float
        Segundo operando.

    Returns
    -------
    float
        A soma a + b.

    Examples
    --------
    >>> add(2, 3)
    5.0
    >>> add(-1.5, 0.5)
    -1.0
    """
    return float(a) + float(b)


def subtract(a: float, b: float) -> float:
    """Subtrai b de a."""
    raise NotImplementedError


def multiply(a: float, b: float) -> float:
    """Multiplica a por b."""
    raise NotImplementedError


def divide(a: float, b: float) -> float:
    """Divide a por b. Levanta ZeroDivisionError se b == 0."""
    raise NotImplementedError


def power(base: float, exp: float) -> float:
    """Retorna base ** exp."""
    raise NotImplementedError


def sqrt(x: float) -> float:
    """Raiz quadrada de x. Levanta ValueError se x < 0."""
    raise NotImplementedError


def factorial(n: int) -> int:
    """
    Fatorial de n (n!).
    - n deve ser inteiro não negativo, caso contrário levanta ValueError.
    """
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """Retorna True se n é primo, False caso contrário."""
    raise NotImplementedError


def mean(data: Sequence[float]) -> float:
    """Média aritmética. Levanta ValueError se data estiver vazia."""
    raise NotImplementedError

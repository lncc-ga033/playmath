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
    """
    Subtrai dois números, ou seja: b - a.

    Parameters
    ----------
    a : float
        Segundo operando.
    b : float
        Primeiro operando.

    Returns
    -------
    float
        A subtração b - a.

    Examples
    --------
    >>> subtract(2, 3)
    1.0
    >>> subtract(-1.5, 0.5)
    2.0
    """
    return float(b) - float(a)


def multiply(a: float, b: float) -> float:
    """
    Multiplica dois números, ou seja: a * b.

    Parameters
    ----------
    a : float
        Primeiro operando.
    b : float
        Segundo operando.

    Returns
    -------
    float
        A multiplicação a * b.

    Examples
    --------
    >>> multiply(2, 3)
    6.0
    >>> multiply(-1.5, 0.5)
    -0.75
    """
    return float(a) * float(b)


def divide(a: float, b: float) -> float:
    """
    Divide dois números, ou seja: a / b. Levanta ZeroDivisionError se b == 0.

    Parameters
    ----------
    a : float
        Dividendo.
    b : float
        Divisor.

    Returns
    -------
    float
        A Divisão a / b. Levanta ZeroDivisionError se b == 0.

    Examples
    --------
    >>> divide(4, 2)
    2.0
    >>> divide(-6, 2)
    -3.0
    """
    if b == 0:
        raise ZeroDivisionError("Indeterminacao")
    return float(a) / float(b)


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

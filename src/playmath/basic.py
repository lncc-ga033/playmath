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


def gcd(a: int, b: int) -> int:
    """Máximo divisor comum (resultado não negativo)."""
    raise NotImplementedError


def lcm(a: int, b: int) -> int:
    """Mínimo múltiplo comum (resultado não negativo)."""
    raise NotImplementedError


def mean(data: Sequence[float]) -> float:
    """Média aritmética. Levanta ValueError se data estiver vazia."""
    raise NotImplementedError


def median(data: Sequence[float]) -> float:
    """Mediana. Levanta ValueError se data estiver vazia."""
    raise NotImplementedError


def variance(data: Sequence[float], *, sample: bool = False) -> float:
    """
    Variância.

    Parameters
    ----------
    data : Sequence[float]
        Amostras numéricas.
    sample : bool, default False
        Se True, usa variância amostral (denominador n-1).
        Caso contrário, variância populacional (denominador n).

    Raises
    ------
    ValueError
        Se data tiver tamanho < 1 (população) ou < 2 (amostra).

    Returns
    -------
    float
        Variância da sequência.
    """
    raise NotImplementedError

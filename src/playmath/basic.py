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
    """
    Calcula a base elevada ao expoente, ou seja: base ^ expoente.

    Parameters
    ----------
    base : float
        Base.
    exp : float
        Expoente.

    Returns
    -------
    float
        O resultado de: base ^ expoente.

    Examples
    --------
    >>> power(2, 3)
    8.0
    >>> power(-2, 3)
    -8.0
    """
    return base**exp


def sqrt(x: float) -> float:
    """
    Calcula raiz quadrada de x, ou seja: sqrt(x). Levanta ValueError se x < 0

    Parameters
    ----------
    x : float
        Valor a ser elevado a 0.5.

    Returns
    -------
    float
        A raiz quadrada de x.

    Examples
    --------
    >>> sqrt(4)
    2.0
    >>> sqrt(9)
    3.0
    """
    if x < 0:
        raise ValueError("Erro, tome x > 0 para obter a raiz quadrada")
    return x**0.5


def factorial(n: int) -> int:
    """
    Calcula o Fatorial de n, ou seja: n!. Levanta ValueError se n não for inteiro negativo

    Parameters
    ----------
    n : int
        Valor a ser calculado o fatorial.

    Returns
    -------
    int
        O resultado do fatorial do n.

    Examples
    --------
    >>> factorial(4)
    24
    >>> factorial(3)
    6
    """
    if n < 0 or n != int(n):
        raise ValueError("Erro, número não inteiro e negativo.")
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return int(fatorial)


def is_prime(n: int) -> bool:
    """
    Verifica se o valor n é primo ou não.

    Parameters
    ----------
    n : int
        Valor a ser verificado.

    Returns
    -------
    bool
        Retorna False ou True.

    Examples
    --------
    >>> is_prime(4)
    Falso
    >>> is_prime(3)
    Verdadeiro
    """
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def mean(data: Sequence[float]) -> float:
    """
    Calcula a média aritmética. Levanta ValueError se data estiver vazia.

    Parameters
    ----------
    data : Sequence[float]
        Valores a serem adicionados em data.

    Returns
    -------
    float
        Retorna a soma aritmética dos valores que estão em data.

    Examples
    --------
    >>> mean([5.0, 4.0, 3.0, 2.0, 1.0])
    3.0
    """
    if len(data) == 0:
        raise ValueError("Erro, data está vazia.")
    return sum(data) / len(data)

# Exemplo de como estruturar novos testes.
# Dica: crie casos simples e alguns extremos (edge cases).


import pytest

from playmath.basic import divide, factorial, is_prime, multiply, power, sqrt, subtract


@pytest.mark.grading
def test_subtract_basic():
    """Teste Básico para a função subtract"""
    assert subtract(2, 3) == 1.0
    assert subtract(-1.5, 0.5) == 2.0


@pytest.mark.grading
def test_multiply_basic():
    """Teste Básico para a função multiply"""
    assert multiply(2, 3) == 6.0
    assert multiply(-1.5, 0.5) == -0.75


@pytest.mark.grading
def test_divide_basic():
    """Teste Básico para a função divide"""
    assert divide(4, 2) == 2.0
    assert divide(-6, 2) == -3.0


@pytest.mark.grading
def test_divide_by_zero():
    """Teste Básico para a função divide com o teste de divisao por zero"""
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)


@pytest.mark.grading
def test_power_basic():
    """Teste Básico para a função power"""
    assert power(2, 3) == 8.0
    assert power(-2, 3) == -8.0


@pytest.mark.grading
def test_sqrt_basic():
    """Teste Básico para a função sqrt"""
    assert sqrt(4) == 2.0
    assert sqrt(9) == 3.0


@pytest.mark.grading
def test_sqrt_negative():
    """Teste Básico para a função sqrt para valores negativos"""
    with pytest.raises(ValueError):
        sqrt(-1)


@pytest.mark.grading
def test_factorial_basic():
    """Teste Básico para a função factorial"""
    assert factorial(4) == 24
    assert factorial(3) == 6


@pytest.mark.grading
def test_is_prime_basic():
    """Teste Básico para a função is_prime"""
    assert is_prime(4) is False
    assert is_prime(3) is True


@pytest.mark.grading
def test_mean_basic():
    # TODO: implemente o corpo após implementar a função
    assert False  # Remova esta linha quando implementar o teste

# Exemplo de como estruturar novos testes.
# Dica: crie casos simples e alguns extremos (edge cases).


import pytest

from playmath.basic import divide, multiply, subtract


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
def test_divide_zero():
    """Teste Básico para a função divide com o teste de divisao por zero"""
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)


@pytest.mark.grading
def test_divide_by_zero():
    # TODO: implemente o corpo após implementar a função
    # Sugestão de uso do pytest para checar exceções
    # with pytest.raises(ZeroDivisionError):
    #     divide(1, 0)
    assert False  # Remova esta linha quando implementar o teste


@pytest.mark.grading
def test_power_basic():
    # TODO: implemente o corpo após implementar a função
    assert False  # Remova esta linha quando implementar o teste


@pytest.mark.grading
def test_sqrt_basic():
    # TODO: implemente o corpo após implementar a função
    assert False  # Remova esta linha quando implementar o teste


@pytest.mark.grading
def test_sqrt_negative():
    # TODO: implemente o corpo após implementar a função
    # with pytest.raises(ValueError):
    #     sqrt(-1.0)
    assert False  # Remova esta linha quando implementar o teste


@pytest.mark.grading
def test_factorial_basic():
    # TODO: implemente o corpo após implementar a função
    assert False  # Remova esta linha quando implementar o teste


@pytest.mark.grading
def test_is_prime_basic():
    # TODO: implemente o corpo após implementar a função
    assert False  # Remova esta linha quando implementar o teste


@pytest.mark.grading
def test_mean_basic():
    # TODO: implemente o corpo após implementar a função
    assert False  # Remova esta linha quando implementar o teste

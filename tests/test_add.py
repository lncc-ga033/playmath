import math

from playmath.basic import add


def test_add_integers():
    assert add(2, 3) == 5.0


def test_add_floats():
    assert math.isclose(add(2.5, 0.5), 3.0)


def test_add_negatives():
    assert add(-1, -2) == -3.0

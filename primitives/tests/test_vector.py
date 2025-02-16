import pytest
from ..vector import Vector


def test_pont_values():
    positions = [3, -5]
    vector = Vector(positions)

    assert vector.positions == positions


def test_pont_add_vector():
    vector_1 = Vector([3, -5])
    vector_2 = Vector([6, 7])

    new_vector = Vector.add(vector_1, vector_2)
    assert new_vector.positions == [9, 2]


def test_pont_add_vector_different_dimensions():
    vector_1 = Vector([3, -5, 2])
    vector_2 = Vector([6, 7])

    with pytest.raises(ValueError):
        Vector.add(vector_1, vector_2)


def test_vectors_equality():
    vector_1 = Vector([6, 7])
    vector_2 = Vector([6, 7])
    vector_3 = Vector([3, 7])
    vector_4 = Vector([6, -5])
    vector_5 = Vector([6, 7, 7])

    assert vector_1 == vector_2
    assert vector_1 != vector_3
    assert vector_1 != vector_4
    assert vector_1 != vector_5


def test_pont_to_string():
    vector = Vector([-5, 4, 6])

    assert str(vector) == 'Vector([-5, 4, 6])'

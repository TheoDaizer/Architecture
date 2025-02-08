from ..vector import Vector


def test_pont_values():
    x, y = 3, -5
    vector = Vector(x, y)

    assert vector.x == x
    assert vector.y == y


def test_pont_add_vector():
    vector_1 = Vector(3, -5)
    vector_2 = Vector(6, 7)

    new_vector = vector_1.add(vector_2)
    assert new_vector.x == 9
    assert new_vector.y == 2

def test_vectors_equality():
    vector_1 = Vector(6, 7)
    vector_2 = Vector(6, 7)
    vector_3 = Vector(3, 7)
    vector_4 = Vector(6, -5)

    assert vector_1 == vector_2
    assert vector_1 != vector_3
    assert vector_1 != vector_4


def test_pont_to_string():
    vector = Vector(-5, 4)

    assert str(vector) == 'Vector(-5, 4)'

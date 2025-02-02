from ..point import Point, Vector


def test_pont_values():
    x, y = 3, -5
    point = Point(x, y)

    assert point.x == x
    assert point.y == y


def test_pont_add_point():
    point_1 = Point(3, -5)
    point_2 = Point(6, 7)

    new_point = point_1.add(point_2)
    assert new_point.x == 9
    assert new_point.y == 2


def test_pont_add_vector():
    point = Point(4, 3)
    vector = Vector(5, 4)

    new_point = point.add(vector)
    assert new_point.x == 9
    assert new_point.y == 7


def test_points_equality():
    point_1 = Point(6, 7)
    point_2 = Point(6, 7)
    point_3 = Point(3, 7)
    point_4 = Point(6, -5)

    assert point_1 == point_2
    assert point_1 != point_3
    assert point_1 != point_4


def test_pont_to_string():
    point = Point(-5, 4)

    assert str(point) == 'Point(-5, 4)'

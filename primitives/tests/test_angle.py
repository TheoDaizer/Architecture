import pytest
from ..angle import Angle


def test_angle_values():
    n, s = 1, 8
    angle = Angle(n, s)

    assert angle.n == n
    assert angle.s == s


def test_different_signifiers_error():
    angle_1 = Angle(5, 8)
    angle_2 = Angle(6, 7)

    with pytest.raises(ValueError):
        angle_1.add(angle_2)


def test_angle_add_angle():
    angle_1 = Angle(5, 8)
    angle_2 = Angle(6, 8)

    new_angle = angle_1.add(angle_2)
    assert new_angle.n == 3
    assert new_angle.s == 8


def test_points_equality():
    angle_1 = Angle(6, 7)
    angle_2 = Angle(6, 7)
    angle_3 = Angle(3, 7)
    angle_4 = Angle(6, -5)

    assert angle_1 == angle_2
    assert angle_1 != angle_3
    assert angle_1 != angle_4


def test_pont_to_string():
    angle = Angle(-5, 4)

    assert str(angle) == 'Angle(-5, 4)'

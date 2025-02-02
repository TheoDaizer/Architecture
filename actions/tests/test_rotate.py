import pytest

from actions import Rotate
from primitives import Angle
from unittest.mock import Mock


def test_rotate():
    mock_rotatable_object = Mock()
    mock_rotatable_object.get_angle.return_value = Angle(6, 8)
    mock_rotatable_object.get_angular_velocity.return_value = Angle(-1, 8)

    rotate = Rotate(mock_rotatable_object)
    rotate.execute()
    mock_rotatable_object.set_angle.assert_called_once_with(Angle(5, 8))

def test_get_angle_error():
    mock_rotatable_object = Mock()
    mock_rotatable_object.get_angle.side_effect = ValueError('Test get_position error')
    mock_rotatable_object.get_angular_velocity.return_value = Angle(-1, 8)

    move = Rotate(mock_rotatable_object)
    with pytest.raises(ValueError):
        move.execute()

def test_get_angular_velocity_error():
    mock_rotatable_object = Mock()
    mock_rotatable_object.get_angle.return_value = Angle(6, 8)
    mock_rotatable_object.get_angular_velocity.side_effect = ValueError('Test get_velocity error')

    move = Rotate(mock_rotatable_object)
    with pytest.raises(ValueError):
        move.execute()

def test_set_angle_error():
    mock_rotatable_object = Mock()
    mock_rotatable_object.get_angle.return_value = Angle(6, 8)
    mock_rotatable_object.get_angular_velocity.return_value = Angle(-1, 8)
    mock_rotatable_object.set_angle.side_effect = ValueError('Test test_set_position error')

    move = Rotate(mock_rotatable_object)
    with pytest.raises(ValueError):
        move.execute()

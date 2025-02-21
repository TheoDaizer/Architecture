import pytest

from commands import RotateVelocityCommand
from primitives import Angle, Vector
from unittest.mock import Mock


def test_rotate_velocity():
    mock_movable_object = Mock()
    mock_movable_object.get_angular_velocity.return_value = Angle(1, 2)
    mock_movable_object.get_velocity.return_value = Vector([-7, 3])

    move = RotateVelocityCommand(mock_movable_object)
    move.execute()
    mock_movable_object.set_velocity.assert_called_once_with(Vector([7, -3]))

def test_get_angle_error():
    mock_movable_object = Mock()
    mock_movable_object.get_angular_velocity.side_effect = ValueError('Test get_angular_velocity error')
    mock_movable_object.get_velocity.return_value = Vector([-7, 3])

    move = RotateVelocityCommand(mock_movable_object)
    with pytest.raises(ValueError):
        move.execute()

def test_get_velocity_error():
    mock_movable_object = Mock()
    mock_movable_object.get_angular_velocity.return_value = Angle(1, 2)
    mock_movable_object.get_velocity.side_effect = ValueError('Test get_velocity error')

    move = RotateVelocityCommand(mock_movable_object)
    with pytest.raises(ValueError):
        move.execute()

def test_set_position_error():
    mock_movable_object = Mock()
    mock_movable_object.get_angular_velocity.return_value = Angle(1, 2)
    mock_movable_object.get_velocity.return_value = Vector([-7, 3])
    mock_movable_object.set_velocity.side_effect = ValueError('Test test_set_position error')

    move = RotateVelocityCommand(mock_movable_object)
    with pytest.raises(ValueError):
        move.execute()

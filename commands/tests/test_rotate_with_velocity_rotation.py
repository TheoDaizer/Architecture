import pytest
from unittest.mock import Mock

from commands.rotate_with_velocity_rotation import RotateWithVelocityRotation
from commands.exceptions import CommandException
from primitives import Angle, Vector


def test_rotate_with_valid_velocity_rotatable_object():
    mock_object = Mock()

    mock_object.get_angle.return_value = Angle(0, 4)
    mock_object.get_angular_velocity.return_value = Angle(2, 4)

    mock_object.is_velocity_rotatable.return_value = True

    mock_object.get_velocity.return_value = Vector([-4, 5])

    command = RotateWithVelocityRotation(mock_object)
    command.execute()

    mock_object.set_angle.assert_called_once_with(Angle(2, 4))
    mock_object.set_velocity.assert_called_once_with(Vector([4, -5]))


def test_rotate_with_not_valid_velocity_rotatable_object():
    mock_object = Mock()

    mock_object.get_angle.return_value = Angle(1, 4)
    mock_object.get_angular_velocity.return_value = Angle(3, 4)

    mock_object.is_velocity_rotatable.return_value = False

    command = RotateWithVelocityRotation(mock_object)
    with pytest.raises(CommandException):
        command.execute()

    mock_object.set_angle.assert_called_once_with(Angle(0, 4))
    mock_object.set_velocity.assert_not_called()

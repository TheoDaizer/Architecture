import pytest
from unittest.mock import Mock

from commands import IsVelocityRotatableObjectCommand
from commands.exceptions import CommandException


def test_check_velocity_rotatable_valid_object():
    mock_is_velocity_rotatable_object = Mock()
    mock_is_velocity_rotatable_object.is_velocity_rotatable.return_value = True

    command = IsVelocityRotatableObjectCommand(mock_is_velocity_rotatable_object)
    command.execute()

    mock_is_velocity_rotatable_object.is_velocity_rotatable.assert_called_once()

def test_velocity_rotatable_not_valid_object():
    mock_is_velocity_rotatable_object = Mock()
    mock_is_velocity_rotatable_object.is_velocity_rotatable.return_value = False

    command = IsVelocityRotatableObjectCommand(mock_is_velocity_rotatable_object)

    with pytest.raises(CommandException):
        command.execute()

    mock_is_velocity_rotatable_object.is_velocity_rotatable.assert_called_once()

def test_is_velocity_rotatable_exception():
    mock_is_velocity_rotatable_object = Mock()
    mock_is_velocity_rotatable_object.is_velocity_rotatable.side_effect = AttributeError

    command = IsVelocityRotatableObjectCommand(mock_is_velocity_rotatable_object)

    with pytest.raises(AttributeError):
        command.execute()

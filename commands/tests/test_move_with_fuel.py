import pytest
from unittest.mock import Mock

from commands.move_with_fuel import MoveWithFuel
from commands.exceptions import CommandException
from primitives import Vector


def test_move_with_fuel_with_enough_fuel():
    mock_object = Mock()

    mock_object.get_position.return_value = Vector([12, 5])
    mock_object.get_velocity.return_value = Vector([-7, 3])

    mock_object.get_fuel_available.return_value = 5
    mock_object.get_fuel_to_burn.return_value = 2

    macro_command = MoveWithFuel(mock_object)

    macro_command.execute()

    mock_object.set_position.assert_called_once_with(Vector([5, 8]))
    mock_object.set_fuel_available.assert_called_once_with(3)


def test_move_with_fuel_with_not_enough_fuel():
    mock_object = Mock()

    mock_object.get_fuel_available.return_value = 3
    mock_object.get_fuel_to_burn.return_value = 7

    macro_command = MoveWithFuel(mock_object)

    with pytest.raises(CommandException):
        macro_command.execute()

    mock_object.set_position.assert_not_called()
    mock_object.set_fuel_available.assert_not_called()

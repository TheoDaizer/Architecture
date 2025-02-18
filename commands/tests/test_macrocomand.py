import pytest
from unittest.mock import Mock

from commands import MacroCommand, CheckFuelCommand, MoveCommand, BurnFuelCommand
from commands.exceptions import CommandException
from primitives import Vector


def test_macro_command():
    mock_command_1 = Mock()
    mock_command_2 = Mock()

    macro_command = MacroCommand([mock_command_1, mock_command_2])
    macro_command.execute()
    mock_command_1.execute.assert_called_once()
    mock_command_2.execute.assert_called_once()


def test_macro_command_exception():
    mock_command_1 = Mock()
    mock_command_2 = Mock()
    mock_command_2.execute.side_effect = CommandException()
    mock_command_3 = Mock()

    macro_command = MacroCommand([mock_command_1, mock_command_2, mock_command_3])

    with pytest.raises(CommandException):
        macro_command.execute()

    mock_command_1.execute.assert_called_once()
    mock_command_2.execute.assert_called_once()
    mock_command_3.execute.assert_not_called()


def test_macro_command_move_and_burn_fuel():
    mock_object = Mock()

    mock_object.get_position.return_value = Vector([12, 5])
    mock_object.get_velocity.return_value = Vector([-7, 3])

    mock_object.get_fuel_available.return_value = 5
    mock_object.get_fuel_to_burn.return_value = 2

    macro_command = MacroCommand([
        CheckFuelCommand(mock_object),
        MoveCommand(mock_object),
        BurnFuelCommand(mock_object),
    ])

    macro_command.execute()

    mock_object.set_position.assert_called_once_with(Vector([5, 8]))
    mock_object.set_fuel_available.assert_called_once_with(3)

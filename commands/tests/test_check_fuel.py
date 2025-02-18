import pytest
from unittest.mock import Mock

from commands import CheckFuelCommand
from commands.exceptions import CommandException


def test_check_fuel():
    mock_fuel_checkable_object = Mock()
    mock_fuel_checkable_object.get_fuel_available.return_value = 2
    mock_fuel_checkable_object.get_fuel_to_burn.return_value = 1

    command = CheckFuelCommand(mock_fuel_checkable_object)
    command.execute()


def test_check_fuel_too_low():
    mock_fuel_checkable_object = Mock()
    mock_fuel_checkable_object.get_fuel_available.return_value = 2
    mock_fuel_checkable_object.get_fuel_to_burn.return_value = 3

    command = CheckFuelCommand(mock_fuel_checkable_object)

    with pytest.raises(CommandException):
        command.execute()


def test_get_fuel_available_error():
    mock_fuel_checkable_object = Mock()
    mock_fuel_checkable_object.get_fuel_available.side_effect = ValueError()
    mock_fuel_checkable_object.get_fuel_to_burn.return_value = 3

    command = CheckFuelCommand(mock_fuel_checkable_object)
    with pytest.raises(ValueError):
        command.execute()


def test_get_fuel_to_burn_error():
    mock_fuel_checkable_object = Mock()
    mock_fuel_checkable_object.get_fuel_available.return_value = 2
    mock_fuel_checkable_object.get_fuel_to_burn.side_effect = ValueError()

    command = CheckFuelCommand(mock_fuel_checkable_object)
    with pytest.raises(ValueError):
        command.execute()

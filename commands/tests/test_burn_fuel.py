import pytest
from unittest.mock import Mock

from commands import BurnFuelCommand


def test_check_fuel():
    mock_fuel_burnable_object = Mock()
    mock_fuel_burnable_object.get_fuel_available.return_value = 5
    mock_fuel_burnable_object.get_fuel_to_burn.return_value = 2

    command = BurnFuelCommand(mock_fuel_burnable_object)
    command.execute()
    mock_fuel_burnable_object.set_fuel_available.assert_called_once_with(3)


def test_get_fuel_available_error():
    mock_fuel_burnable_object = Mock()
    mock_fuel_burnable_object.get_fuel_available.side_effect = ValueError('Test get_position error')
    mock_fuel_burnable_object.get_fuel_to_burn.return_value = 2

    command = BurnFuelCommand(mock_fuel_burnable_object)
    with pytest.raises(ValueError):
        command.execute()

def test_get_fuel_to_burn_error():
    mock_fuel_burnable_object = Mock()
    mock_fuel_burnable_object.get_fuel_available.return_value = 5
    mock_fuel_burnable_object.get_fuel_to_burn.side_effect = ValueError('Test get_velocity error')

    command = BurnFuelCommand(mock_fuel_burnable_object)
    with pytest.raises(ValueError):
        command.execute()

def test_set_fuel_available_error():
    mock_fuel_burnable_object = Mock()
    mock_fuel_burnable_object.get_fuel_available.return_value = 5
    mock_fuel_burnable_object.get_fuel_to_burn.return_value = 2
    mock_fuel_burnable_object.set_fuel_available.side_effect = ValueError('Test test_set_position error')

    command = BurnFuelCommand(mock_fuel_burnable_object)
    with pytest.raises(ValueError):
        command.execute()

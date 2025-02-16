import pytest

from commands import MoveCommand
from primitives import Vector
from unittest.mock import Mock


def test_move():
    mock_movable_object = Mock()
    mock_movable_object.get_position.return_value = Vector([12, 5])
    mock_movable_object.get_velocity.return_value = Vector([-7, 3])

    move = MoveCommand(mock_movable_object)
    move.execute()
    mock_movable_object.set_position.assert_called_once_with(Vector([5, 8]))

def test_get_position_error():
    mock_movable_object = Mock()
    mock_movable_object.get_position.side_effect = ValueError('Test get_position error')
    mock_movable_object.get_velocity.return_value = Vector([-7, 3])

    move = MoveCommand(mock_movable_object)
    with pytest.raises(ValueError):
        move.execute()

def test_get_velocity_error():
    mock_movable_object = Mock()
    mock_movable_object.get_position.return_value = Vector([12, 5])
    mock_movable_object.get_velocity.side_effect = ValueError('Test get_velocity error')

    move = MoveCommand(mock_movable_object)
    with pytest.raises(ValueError):
        move.execute()

def test_set_position_error():
    mock_movable_object = Mock()
    mock_movable_object.get_position.return_value = Vector([12, 5])
    mock_movable_object.get_velocity.return_value = Vector([-7, 3])
    mock_movable_object.set_position.side_effect = ValueError('Test test_set_position error')

    move = MoveCommand(mock_movable_object)
    with pytest.raises(ValueError):
        move.execute()

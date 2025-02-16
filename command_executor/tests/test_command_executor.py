import pytest
from unittest.mock import Mock

from command_executor.command_executor import CommandExecutor
from primitives.command_queue import CommandQueue


def test_command_executor():
    mock_command = Mock()
    exception_mapper = Mock()

    command_queue = CommandQueue()
    command_queue.put(mock_command)

    command_executor = CommandExecutor(command_queue, exception_mapper)
    command_executor.execute()

    mock_command.execute.assert_called_once()
    exception_mapper.assert_not_called()

def test_command_executor_unknown_error():
    mock_command = Mock()
    mock_command.execute.side_effect = Exception('Test error')
    exception_mapper = Mock()
    exception_mapper.get_handler.return_value = None

    command_queue = CommandQueue()
    command_queue.put(mock_command)

    command_executor = CommandExecutor(command_queue, exception_mapper)

    with pytest.raises(Exception):
        command_executor.execute()

    mock_command.execute.assert_called_once()
    exception_mapper.get_handler.assert_called_once()

def test_command_executor_handle_error():
    mock_command = Mock()
    mock_command.execute.side_effect = Exception('Test error')
    exception_mapper = Mock()
    mock_handler_type = Mock()
    exception_mapper.get_handler.return_value = mock_handler_type

    command_queue = CommandQueue()
    command_queue.put(mock_command)

    command_executor = CommandExecutor(command_queue, exception_mapper)
    command_executor.execute()

    mock_command.execute.assert_called_once()
    exception_mapper.get_handler.assert_called_once()

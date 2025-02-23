from unittest.mock import Mock

from exception_handlers.handlers.log_exception_handler import LogExceptionCommand, LogExceptionHandler
from primitives.command_queue import CommandQueue


def test_log_error_handler():
    mock_command = Mock()
    mock_error = Exception('Test Exception')
    mock_commands_deque = CommandQueue()

    log_exception_handler = LogExceptionHandler(mock_commands_deque, mock_command, mock_error)
    log_exception_handler.execute()

    assert len(mock_commands_deque) == 1
    assert isinstance(mock_commands_deque.head(), LogExceptionCommand)

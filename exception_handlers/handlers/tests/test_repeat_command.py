from collections import deque
from unittest.mock import Mock

from exception_handlers.handlers.repeat_handler import RepeatCommand, RepeatCommandHandler


def test_log_error_handler():
    mock_command = Mock()
    mock_error = Exception('Test Exception')
    mock_commands_deque = deque()

    log_exception_handler = RepeatCommandHandler(mock_commands_deque, mock_command, mock_error)
    log_exception_handler.execute()

    assert len(mock_commands_deque) == 1
    assert isinstance(mock_commands_deque.pop(), RepeatCommand)

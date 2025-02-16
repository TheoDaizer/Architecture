import pytest
from unittest.mock import Mock

from exception_handlers.commands import RepeatCommand, ReRepeatCommand


@pytest.mark.parametrize("repeat_command_class", [RepeatCommand, ReRepeatCommand])
def test_repeat_command(repeat_command_class):
    mock_command = Mock()
    mock_error = Exception('Test Exception')

    log_exception_command  = repeat_command_class(mock_command, mock_error)
    log_exception_command.execute()

    mock_command.execute.assert_called_once()

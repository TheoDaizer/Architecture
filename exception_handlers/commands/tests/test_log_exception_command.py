from unittest.mock import Mock, patch

from exception_handlers.commands import LogExceptionCommand


@patch('exception_handlers.commands.log_exception_command.getLogger')
def test_log_error_command(mock_get_logger):
    class MockCommand:
        def execute(self):
            pass

    mock_command = MockCommand()
    mock_error = Exception('Test Exception')

    mock_logger = Mock()
    mock_get_logger.return_value = mock_logger

    log_exception_command  = LogExceptionCommand(mock_command, mock_error)
    log_exception_command.execute()

    mock_get_logger.assert_called_once_with('MockCommand Exception')
    mock_logger.error.assert_called_once_with(mock_error)

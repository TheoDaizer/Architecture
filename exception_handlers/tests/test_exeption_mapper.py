from exception_handlers.exception_mapper import ExceptionMapper
from exception_handlers.commands import RepeatCommand, LogExceptionCommand
from exception_handlers.handlers import LogExceptionHandler


def test_exception_mapper():
    repeat_command_map = {RepeatCommand: {ValueError: LogExceptionHandler}}
    exception_mapper = ExceptionMapper(repeat_command_map)

    mock_error = ValueError()
    mock_command = RepeatCommand(LogExceptionCommand, mock_error)

    handler = exception_mapper.get_handler(mock_command, mock_error)

    assert handler is LogExceptionHandler

def test_exception_mapper_unknown_command():
    repeat_command_map = {RepeatCommand: {ValueError: LogExceptionHandler}}
    exception_mapper = ExceptionMapper(repeat_command_map)

    mock_error = ValueError()
    mock_command = LogExceptionCommand(LogExceptionCommand, mock_error)

    handler = exception_mapper.get_handler(mock_command, mock_error)

    assert handler is None

def test_exception_mapper_unknown_error():
    repeat_command_map = {RepeatCommand: {ValueError: LogExceptionHandler}}
    exception_mapper = ExceptionMapper(repeat_command_map)

    mock_error = TypeError()
    mock_command = RepeatCommand(LogExceptionCommand, mock_error)

    handler = exception_mapper.get_handler(mock_command, mock_error)

    assert handler is None

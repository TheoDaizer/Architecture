from collections import deque
from unittest.mock import Mock

from command_executor.command_executor import CommandExecutor
from exception_handlers.exception_mapper import ExceptionMapper
from exception_handlers.commands import RepeatCommand, ReRepeatCommand, LogExceptionCommand
from exception_handlers.handlers import RepeatCommandHandler, ReRepeatCommandHandler, LogExceptionHandler


def test_repeat_and_log_scenario():
    mock_error = Exception()
    mock_command = Mock()
    mock_command.execute.side_effect = mock_error
    exception_map = {
        type(mock_command): {type(mock_error): RepeatCommandHandler},
        RepeatCommand: {type(mock_error): LogExceptionHandler},
    }

    exception_mapper = ExceptionMapper(exception_map)

    command_deque = deque()
    command_deque.append(mock_command)

    command_executor = CommandExecutor(command_deque, exception_mapper)
    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque[0]) is RepeatCommand

    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque[0]) is LogExceptionCommand


def test_command_executor():
    mock_error = Exception()
    mock_command = Mock()
    mock_command.execute.side_effect = mock_error
    exception_map = {
        type(mock_command): {type(mock_error): RepeatCommandHandler},
        RepeatCommand: {type(mock_error): ReRepeatCommandHandler},
        ReRepeatCommand: {type(mock_error): LogExceptionHandler},
    }

    exception_mapper = ExceptionMapper(exception_map)

    command_deque = deque()
    command_deque.append(mock_command)

    command_executor = CommandExecutor(command_deque, exception_mapper)
    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque[0]) is RepeatCommand

    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque[0]) is ReRepeatCommand

    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque[0]) is LogExceptionCommand

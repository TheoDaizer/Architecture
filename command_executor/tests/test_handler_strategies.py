from unittest.mock import Mock

from command_executor.command_executor import CommandExecutor
from primitives.command_queue import CommandQueue
from exception_handlers.exception_mapper import ExceptionMapper
from exception_handlers.commands import RepeatCommand, ReRepeatCommand, LogExceptionCommand
from exception_handlers.handlers import RepeatCommandHandler, ReRepeatCommandHandler, LogExceptionHandler


def test_repeat_and_log_scenario():
    mock_error = Exception()
    mock_command = Mock()
    mock_command.execute.side_effect = mock_error

    exception_mapper = ExceptionMapper()
    exception_mapper.register_handler(type(mock_command), type(mock_error), RepeatCommandHandler)
    exception_mapper.register_handler(RepeatCommand, type(mock_error), LogExceptionHandler)

    command_deque = CommandQueue()
    command_deque.put(mock_command)

    command_executor = CommandExecutor(command_deque, exception_mapper)
    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque.head()) is RepeatCommand

    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque.head()) is LogExceptionCommand


def test_command_executor():
    mock_error = Exception()
    mock_command = Mock()
    mock_command.execute.side_effect = mock_error

    exception_mapper = ExceptionMapper()
    exception_mapper.register_handler(type(mock_command), type(mock_error), RepeatCommandHandler)
    exception_mapper.register_handler(RepeatCommand, type(mock_error), ReRepeatCommandHandler)
    exception_mapper.register_handler(ReRepeatCommand, type(mock_error), LogExceptionHandler)

    command_deque = CommandQueue()
    command_deque.put(mock_command)

    command_executor = CommandExecutor(command_deque, exception_mapper)
    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque.head()) is RepeatCommand

    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque.head()) is ReRepeatCommand

    command_executor.execute()

    assert len(command_deque) == 1
    assert type(command_deque.head()) is LogExceptionCommand

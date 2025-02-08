from collections import deque

from actions.command_interface import Command
from exception_handlers.commands import LogExceptionCommand


class LogExceptionHandler:
    def __init__(self, command_deque: deque[Command], command_to_handel: Command, exception: Exception):
        self.deque = command_deque
        self.command_to_handel = command_to_handel
        self.exception = exception

    def execute(self):
        command = LogExceptionCommand(self.command_to_handel, self.exception)
        self.deque.append(command)

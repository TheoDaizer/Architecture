from ioc.i_command import Command
from exception_handlers.commands import LogExceptionCommand
from primitives.command_queue import CommandQueue


class LogExceptionHandler:
    def __init__(self, command_queue: CommandQueue, command_to_handel: Command, exception: Exception):
        self.command_queue = command_queue
        self.command_to_handel = command_to_handel
        self.exception = exception

    def execute(self):
        command = LogExceptionCommand(self.command_to_handel, self.exception)
        self.command_queue.put(command)

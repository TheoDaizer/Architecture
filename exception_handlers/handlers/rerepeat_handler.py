from actions.command_interface import Command
from exception_handlers.commands import ReRepeatCommand
from primitives.command_queue import CommandQueue


class ReRepeatCommandHandler:
    def __init__(self, command_queue: CommandQueue, command_to_handel: Command, exception: Exception):
        self.command_queue = command_queue
        self.command_to_handel = command_to_handel
        self.exception = exception

    def execute(self):
        command = ReRepeatCommand(self.command_to_handel, self.exception)
        self.command_queue.put(command)

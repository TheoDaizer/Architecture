from actions.command_interface import Command
from exception_handlers.commands import RepeatCommand
from primitives.command_queue import CommandQueue


class RepeatCommandHandler:
    def __init__(self, command_queue: CommandQueue, command_to_handel: Command, exception: Exception):
        self.command_queue = command_queue
        self.command_to_handel = command_to_handel
        self.exception = exception

    def execute(self):
        command = RepeatCommand(self.command_to_handel, self.exception)
        self.command_queue.put(command)

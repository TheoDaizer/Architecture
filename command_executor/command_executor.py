from collections import deque
from actions.command_interface import Command
from exception_handlers.exception_mapper import ExceptionMapper


class CommandExecutor:
    def __init__(self, command_deque: deque[Command], exception_handler: ExceptionMapper):
        self.deque = command_deque
        self.exception_handler = exception_handler

    def execute(self):
        command = self.deque.popleft()
        try:
            command.execute()
        except Exception as error:
            handler_type = self.exception_handler.get_handler(command, error)

            if handler_type is None:
                raise error

            handler: Command = handler_type(self.deque, command, error)
            handler.execute()

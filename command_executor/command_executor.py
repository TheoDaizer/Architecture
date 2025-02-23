from ioc.i_command import Command
from primitives.command_queue import CommandQueue
from exception_handlers.exception_mapper import ExceptionMapper


class CommandExecutor:
    def __init__(self, queue: CommandQueue, exception_handler: ExceptionMapper):
        self.queue = queue
        self.exception_handler = exception_handler

    def execute(self):
        command = self.queue.get()
        try:
            command.execute()
        except Exception as error:
            handler_type = self.exception_handler.get_handler(command, error)

            if handler_type is None:
                raise error

            handler: Command = handler_type(self.queue, command, error)
            handler.execute()

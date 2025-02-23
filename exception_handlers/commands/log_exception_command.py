from logging import getLogger
from actions.command_interface import Command


class LogExceptionCommand:
    def __init__(self, command_to_handel: Command, exception: Exception):
        self.command_to_handel = command_to_handel
        self.exception = exception

        self.logger = getLogger(f'{type(command_to_handel).__name__} Exception')

    def execute(self):
        self.logger.error(self.exception)

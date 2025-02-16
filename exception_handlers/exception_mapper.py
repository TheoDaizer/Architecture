from typing import Type
from actions.command_interface import Command


class ExceptionMapper:

    def __init__(self):
        self.exceptions_map = {}

    def register_handler(self, command_type: Type, exception_type: Type, handler: Command):
        if command_type not in  self.exceptions_map:
            self.exceptions_map[command_type] = {}

        command_error_handlers = self.exceptions_map[command_type]
        command_error_handlers[exception_type] = handler

    def get_handler(self, command_to_handel: Command, exception: Exception):
        command_error_handlers = self.exceptions_map.get(type(command_to_handel), {})
        error_handler = command_error_handlers.get(type(exception))

        return error_handler

from typing import Type
from actions.command_interface import Command


class ExceptionMapper:

    def __init__(self, exceptions_map: dict):
        self.exceptions_map: dict[Type, dict[Type[Exception], Type]] = exceptions_map

    def get_handler(self, command_to_handel: Command, exception: Exception):
        command_error_handlers = self.exceptions_map.get(type(command_to_handel), {})
        error_handler = command_error_handlers.get(type(exception))

        return error_handler

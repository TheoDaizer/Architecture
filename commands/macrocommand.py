from typing import Iterable
from ioc.i_command import Command
from commands.exceptions import CommandException


class MacroCommand:
    """Simple command to run array of commands"""

    def __init__(self, commands = Iterable[Command]):
        self.commands = tuple(commands)

    def execute(self):
        try:
            for command in self.commands:
                command.execute()
        except:
            raise CommandException

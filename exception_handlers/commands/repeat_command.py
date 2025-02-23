from ioc.i_command import Command


class RepeatCommand:
    def __init__(self, command_to_handel: Command, exception: Exception):
        self.command_to_handel = command_to_handel
        self.exception = exception

    def execute(self):
        self.command_to_handel.execute()


class ReRepeatCommand(RepeatCommand):
    pass

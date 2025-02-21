from typing import Protocol


class Command(Protocol):
    """Command interface"""

    def execute(self):
        """Run command."""
        ...

from typing import Protocol
from commands.exceptions import CommandException


class IsVelocityRotatableObject(Protocol):

    def is_velocity_rotatable(self) -> bool:
        ...


class IsVelocityRotatableObjectCommand:
    """Command to check if object is VelocityRotatable"""

    def __init__(self, obj: IsVelocityRotatableObject):
        self.obj = obj

    def execute(self):
        if not self.obj.is_velocity_rotatable():
            raise CommandException('Object not VelocityRotatable')

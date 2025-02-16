from typing import Protocol
from primitives import Vector


class MovableObject(Protocol):

    def get_position(self) -> Vector:
        ...

    def get_velocity(self) -> Vector:
        ...

    def set_position(self, new_position: Vector):
        ...


class MoveCommand:
    """Class to move objects in space"""

    def __init__(self, obj: MovableObject):
        self.obj = obj

    def execute(self):
        position = self.obj.get_position()
        velocity = self.obj.get_velocity()

        new_position = Vector.add(position, velocity)

        self.obj.set_position(new_position)

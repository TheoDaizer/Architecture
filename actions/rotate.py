from typing import Protocol
from primitives import Angle


class RotatableObject(Protocol):

    def get_angle(self) -> Angle:
        ...

    def get_angular_velocity(self) -> Angle:
        ...

    def set_angle(self, new_angle: Angle):
        ...


class Rotate:
    """Class to rotate objects"""

    def __init__(self, obj: RotatableObject):
        self.obj = obj

    def execute(self):
        angle = self.obj.get_angle()
        angular_velocity = self.obj.get_angular_velocity()

        new_position = angle.add(angular_velocity)

        self.obj.set_angle(new_position)

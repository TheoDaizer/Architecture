from typing import Protocol
from primitives import Angle, Vector


class VelocityRotatableObject(Protocol):

    def get_angular_velocity(self) -> Angle:
        ...

    def get_velocity(self) -> Vector:
        ...

    def set_velocity(self, new_vector: Vector):
        ...


class RotateVelocityCommand:
    """Class to rotate velocity vector"""

    def __init__(self, obj: VelocityRotatableObject):
        self.obj = obj

    def execute(self):
        angle = self.obj.get_angular_velocity()
        velocity = self.obj.get_velocity()

        new_velocity = Vector.rotate(velocity, angle)

        self.obj.set_velocity(new_velocity)

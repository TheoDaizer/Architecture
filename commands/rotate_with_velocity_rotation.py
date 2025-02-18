from commands import MacroCommand, RotateCommand, RotateVelocityCommand, IsVelocityRotatableObjectCommand
from commands import RotatableObject, VelocityRotatableObject, IsVelocityRotatableObject


class RotateWithVelocityRotation:
    """Class to rotate objects and rotate velocity vector"""

    def __init__(self, obj: RotatableObject | VelocityRotatableObject | IsVelocityRotatableObject):
        self.macro = MacroCommand([
            RotateCommand(obj),
            IsVelocityRotatableObjectCommand(obj),
            RotateVelocityCommand(obj),
        ])

    def execute(self):
        self.macro.execute()

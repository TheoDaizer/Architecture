from commands import MacroCommand, CheckFuelCommand, MoveCommand, BurnFuelCommand
from commands import MovableObject, FuelCheckableObject, FuelBurnableObject


class MoveWithFuel:
    """Class to move objects in space and burn fuel"""

    def __init__(self, obj: MovableObject | FuelCheckableObject | FuelBurnableObject):
        self.macro = MacroCommand([
            CheckFuelCommand(obj),
            MoveCommand(obj),
            BurnFuelCommand(obj),
        ])

    def execute(self):
        self.macro.execute()

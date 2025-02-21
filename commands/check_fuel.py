from typing import Protocol
from commands.exceptions import CommandException


class FuelCheckableObject(Protocol):

    def get_fuel_available(self) -> int:
        ...

    def get_fuel_to_burn(self) -> int:
        ...


class CheckFuelCommand:
    """Class to check fuel of objects"""

    def __init__(self, obj: FuelCheckableObject):
        self.obj = obj

    def execute(self):
        fuel_available = self.obj.get_fuel_available()
        fuel_to_burn = self.obj.get_fuel_to_burn()

        if fuel_available < fuel_to_burn:
            raise CommandException('Available fuel is less then needed')

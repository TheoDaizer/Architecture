from typing import Protocol


class FuelBurnableObject(Protocol):

    def get_fuel_available(self) -> int:
        ...

    def get_fuel_to_burn(self) -> int:
        ...

    def set_fuel_available(self, new_fuel_available: int):
        ...


class BurnFuelCommand:
    """Class to decrease fuel of objects"""

    def __init__(self, obj: FuelBurnableObject):
        self.obj = obj

    def execute(self):
        fuel_available = self.obj.get_fuel_available()
        fuel_to_burn = self.obj.get_fuel_to_burn()

        self.obj.set_fuel_available(fuel_available - fuel_to_burn)

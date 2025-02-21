from math import sin, cos
from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from primitives import Angle


class Vector:
    """Position in discrete space"""

    def __init__(self, positions: Iterable[int]):
        """
        :param positions: position values
        """
        self.positions = list(positions)

    @property
    def dimensions(self) -> int:
        """
        Number of vector dimensions
        """
        return len(self.positions)

    @staticmethod
    def add(vector1: 'Vector', vector2: 'Vector') -> 'Vector':
        """
        Create new vector from summ of two vectors

        :param vector1: first vector
        :param vector2: second vector
        :return: new point
        """
        if vector1.dimensions != vector2.dimensions:
            raise ValueError("Number of dimension in vectors are not equal.")
        return Vector(map(sum, zip(vector1.positions, vector2.positions)))

    @staticmethod
    def rotate(vector: 'Vector', angle: 'Angle') -> 'Vector':
        if vector.dimensions != 2:
            raise ValueError("Supported rotation only for 2D vectors")
        x, y = vector.positions
        radians = angle.as_radians()

        calc_cos = cos(radians)
        calc_sin = sin(radians)

        new_x = round(x * calc_cos - y * calc_sin)
        new_y = round(x * calc_sin + y * calc_cos)

        return Vector([new_x, new_y])

    def __eq__(self, other: 'Vector') -> bool:

        return self.dimensions == other.dimensions and self.positions == other.positions

    def __repr__(self) -> str:
        return 'Vector({})'.format(self.positions)

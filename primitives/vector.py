from typing import Iterable


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

    def __eq__(self, other: 'Vector') -> bool:

        return self.dimensions == other.dimensions and self.positions == other.positions

    def __repr__(self) -> str:
        return 'Vector({})'.format(self.positions)

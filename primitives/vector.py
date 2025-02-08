class Vector:
    """Position in 2D discrete space"""

    def __init__(self, x: int, y: int):
        """
        :param x: x position value
        :param y: y position value
        """
        self.x = x
        self.y = y

    def add(self, other: 'Vector') -> 'Vector':
        """
        Create new point from current and other point

        :param other: other point
        :return: new point
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y


    def __repr__(self) -> str:
        return 'Vector({}, {})'.format(self.x, self.y)

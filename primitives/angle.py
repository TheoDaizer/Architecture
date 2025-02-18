from math import pi

class Angle:
    """Angle as a rational fraction"""

    def __init__(self, n: int, s: int):
        """
        :param n: numerator
        :param s: signifier
        """
        self.n = n
        self.s = s

    def add(self, other: 'Angle') -> 'Angle':
        """
        Create new angle from current and other point

        :param other: other point
        :return: new point
        """
        if self.s != other.s:
            raise ValueError(f"Angle signifiers should be equal")

        new_n = (self.n + other.n) % self.s
        return Angle(new_n, self.s)

    def as_radians(self) -> float:
        return self.n / self.s * 2 * pi

    def __eq__(self, other: 'Angle') -> bool:
        return self.n == other.n and self.s == other.s


    def __repr__(self) -> str:
        return 'Angle({}, {})'.format(self.n, self.s)

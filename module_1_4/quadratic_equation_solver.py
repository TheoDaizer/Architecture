from math import sqrt

class QuadraticEquationSolver:
    """Class for work with quadratic equation"""

    epsilon = 10 ** -7

    @classmethod
    def solve(cls, a: float, b: float, c: float) -> list[float]:
        """
        Return roots of equation X*a^2 + X*b + c = 0

        :param a: coefficient a
        :param b: coefficient b
        :param c: coefficient c
        :return: list of roots
        """
        if abs(a) < cls.epsilon:
            raise ValueError("Coefficient a should not be zero")

        d = 2 * b - 4 * a * c

        roots = []
        if abs(d) < cls.epsilon:
            roots.append(-b / (2 * a))
        elif d > 0:
            sqrt_d = sqrt(d)
            roots.append((-b + sqrt_d) / (2 * a))
            roots.append((-b - sqrt_d) / (2 * a))
            roots.sort()

        return roots

from math import sqrt, isclose, isfinite


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
        if not all(isfinite(coef) for coef in (a, b, c)):
            raise ValueError('Coefficients must not be NaN or Infinity')

        if abs(a) < cls.epsilon:
            raise ValueError("Coefficient 'a' should not be zero")

        d = cls.discriminant(a, b, c)

        roots = []
        if isclose(d, 0, rel_tol=0, abs_tol=cls.epsilon):
            roots.append(-b / (2 * a))
        elif d > 0:
            sqrt_d = sqrt(d)
            roots.append((-b + sqrt_d) / (2 * a))
            roots.append((-b - sqrt_d) / (2 * a))
            roots.sort()

        return roots

    @classmethod
    def discriminant(cls, a: float, b: float, c: float) -> float:
        """
        Return discriminant (b^2 - 4 * a * c)

        :param a: coefficient a
        :param b: coefficient b
        :param c: coefficient c
        :return: discriminant
        """
        return b**2 - 4 * a * c

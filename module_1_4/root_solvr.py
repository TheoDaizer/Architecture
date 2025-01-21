from math import isfinite, sqrt


class RootSolver:

    epsilon = 1e-7

    @classmethod
    def solve(cls, a: float, b: float, c: float) -> list[float]:

        if not all(isfinite(coef) for coef in (a, b, c)):
            raise ValueError('All coefficients must not be NaN oi Infinity')

        if abs(a) < cls.epsilon:
            raise ValueError('Coefficient "a" could not be zero')

        d = b * b - 4 * a * c
        roots = []
        if abs(d) < cls.epsilon:
            roots.append(-b / (2 * a))
        elif d > 0:
            d_sqr = sqrt(d)
            roots.append((-b + d_sqr) / (2 * a))
            roots.append((-b - d_sqr) / (2 * a))

        return roots

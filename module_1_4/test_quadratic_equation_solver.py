import pytest
from math import isclose, nan, inf
from .quadratic_equation_solver import QuadraticEquationSolver


class TestUM:
    @classmethod
    def setup_class(cls):
        cls.epsilon = QuadraticEquationSolver.epsilon
        cls.solver = QuadraticEquationSolver

    def check_result(self, reference, result):

        assert len(result) == len(reference)
        assert all(isclose(result[i], reference[i], rel_tol=0, abs_tol=self.epsilon) for i in range(len(reference)))

    def test_no_roots(self):
        a, b, c = 1.0, 0.0 , 1.0
        reference = tuple()
        result = self.solver.solve(a, b, c)

        self.check_result(reference, result)

    def test_two_roots(self):
        a, b, c = 1.0, 0.0, -1.0
        reference = (-1.0, 1.0)
        result = self.solver.solve(a, b, c)

        self.check_result(reference, result)

    def test_one_root(self):
        a, b, c = 1.0, 2.0, 1.0
        reference = (-1.0,)
        result = self.solver.solve(a, b, c)
        d = self.solver.discriminant(a, b, c)

        assert d == 0
        self.check_result(reference, result)

    def test_one_root_for_non_zero_d(self):
        a, b, c = 1.0, 2.0, 1.0 + self.epsilon / 8
        reference = (-1.0,)
        result = self.solver.solve(a, b, c)
        d = self.solver.discriminant(a, b, c)

        assert d != 0
        self.check_result(reference, result)

    def test_a_equal_zero(self):
        a, b, c = 0.0, 0.0, 0.0
        with pytest.raises(ValueError):
            self.solver.solve(a, b, c)

    def test_a_smaller_then_epsilon(self):
        a, b, c = self.solver.epsilon / 2, 0 , 0
        with pytest.raises(ValueError):
            self.solver.solve(a, b, c)

    def test_nan_inf_coefficients(self):
        a, b, c = nan, nan, nan
        with pytest.raises(ValueError):
            self.solver.solve(a, b, c)

        a, b, c = inf, inf, inf
        with pytest.raises(ValueError):
            self.solver.solve(a, b, c)

        a, b, c = -inf, -inf, -inf
        with pytest.raises(ValueError):
            self.solver.solve(a, b, c)

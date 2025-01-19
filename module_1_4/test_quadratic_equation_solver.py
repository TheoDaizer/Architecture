import pytest
from .quadratic_equation_solver import QuadraticEquationSolver


class TestUM:
    @classmethod
    def setup_class(cls):
        cls.epsilon = QuadraticEquationSolver.epsilon
        cls.solver = QuadraticEquationSolver

    def check_result(self, reference, result):

        assert len(result) == len(reference)
        assert all(abs(result[i] - reference[i]) < self.epsilon for i in range(len(reference)))

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

        self.check_result(reference, result)

    def test_one_non_int_root(self):
        a, b, c = 0.55, 3.3, 3.0
        reference = (-3.0,)
        result = self.solver.solve(a, b, c)

        self.check_result(reference, result)

    def test_a_equal_zero(self):
        a, b, c = 0.0, 0.0, 0.0
        with pytest.raises(ValueError):
            self.solver.solve(a, b, c)

    def test_a_smaller_then_epsilon(self):
        a, b, c = self.solver.epsilon / 2, 0 , 0
        with pytest.raises(ValueError):
            self.solver.solve(a, b, c)

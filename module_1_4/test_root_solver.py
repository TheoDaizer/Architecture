import pytest
from math import nan, inf
from .root_solvr import RootSolver


def test_a_is_zero():
    a, b, c = RootSolver.epsilon / 2, 1, 1.0
    with pytest.raises(ValueError):
        RootSolver.solve(a, b, c)

@pytest.mark.parametrize(
    "a, b, c",
    [
        (nan, 1, 1), (1, nan, 1), (1, 1, nan),
        (inf, 1, 1), (1, inf, 1), (1, 1, inf),
        (-inf, 1, 1), (1, -inf, 1), (1, 1, -inf)
    ]
)
def test_not_finite(a, b, c):
    with pytest.raises(ValueError):
        RootSolver.solve(a, b, c)

def test_no_roots():
    a, b, c = 1.0, 0.0, 1.0
    roots = RootSolver.solve(a, b, c)
    result = []

    assert roots == result

def test_one_root():
    a, b, c = 1.0 + RootSolver.epsilon / 8, 2.0, 1.0
    roots = RootSolver.solve(a, b, c)
    result = [-1]

    assert len(result) == len(roots)
    pytest.approx(result, roots, abs=RootSolver.epsilon)

def test_two_roots():
    a, b, c = 1.0, 0.0, -1.0
    roots = RootSolver.solve(a, b, c)
    result = [-1, 1]

    assert len(result) == len(roots)
    pytest.approx(roots, result, abs=RootSolver.epsilon)

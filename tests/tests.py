import numpy as np
from backend.model.solver import least_squares_svd

def test_svd_solver():
    A = np.array([[1, 1], [1, 2], [1, 3]])
    b = np.array([1, 2, 2])
    w = least_squares_svd(A, b)
    assert len(w) == 2
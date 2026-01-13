import numpy as np

def least_squares_svd(A, b):
    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    error = 1e-10
    S_inv = np.diag([1/s if s > error else 0 for s in S])

    w = Vt.T @ S_inv @ U.T @ b
    return w
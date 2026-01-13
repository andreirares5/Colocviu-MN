import numpy as np

def householder_reflector(x):
    """
    Construiește reflectorul Householder pentru vectorul x.
    Returnează vectorul v și scalarul beta astfel încât:
    H = I - beta * v * v^T
    """
    x = x.astype(float)
    sigma = np.dot(x[1:], x[1:])
    v = x.copy()

    if sigma == 0 and x[0] >= 0:
        beta = 0
    elif sigma == 0 and x[0] < 0:
        beta = -2
    else:
        mu = np.sqrt(x[0]**2 + sigma)
        if x[0] <= 0:
            v[0] = x[0] - mu
        else:
            v[0] = -sigma / (x[0] + mu)
        beta = 2 * v[0]**2 / (sigma + v[0]**2)
        v = v / v[0]

    return v, beta


def qr_decomposition(A):
    """
    Realizează factorizarea QR a matricei A folosind reflectori Householder.
    Returnează Q și R.
    """
    A = A.copy().astype(float)
    m, n = A.shape
    Q = np.eye(m)

    for k in range(n):
        # Construim reflectorul pentru coloana k
        x = A[k:, k]
        v, beta = householder_reflector(x)

        # Aplicăm reflectorul pe A
        H = np.eye(m)
        H_k = np.eye(m - k) - beta * np.outer(v, v)
        H[k:, k:] = H_k
        A = H @ A

        # Actualizăm Q
        Q = Q @ H

    R = A
    return Q, R


def solve_least_squares(A, y):
    """
    Rezolvă problema de minime pătrate Aβ ≈ y folosind QR cu reflectori.
    """
    Q, R = qr_decomposition(A)

    # Calculăm Q^T y
    Qt_y = Q.T @ y

    # Extragem partea superioară a lui R (sistemul triunghiular)
    n = A.shape[1]
    R1 = R[:n, :n]
    c1 = Qt_y[:n]

    # Rezolvăm R1 * beta = c1 prin substituție înapoi
    beta = np.zeros(n)
    for i in range(n - 1, -1, -1):
        beta[i] = (c1[i] - np.dot(R1[i, i+1:], beta[i+1:])) / R1[i, i]

    return beta
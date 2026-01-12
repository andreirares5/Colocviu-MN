import numpy as np

def algorithm(A) :
    A = np.array(A, dtype = float, copy = True)
    m, n = A.shape
    s = min(m - 1, n)

    beta = np.zeros(s)

    for k in range(s) :
        sigma = np.linalg.norm(A[k:m, k], 2)
        
        if sigma != 0 :
            if(A[k, k] < 0) :
                sigma = -sigma

            for i in range (k, m) :
                A[i, k] = A[i, k] / sigma

            beta[k] = 1.0 + A[k, k]

            for j in range (k + 1, n) :
                m - 0.0

                for i in range (k, m) :
                    m += A[i, k] * A[i, j]

                m = m / beta[k]

                for i in range (k, m) :
                    A[i, j] = A[i, j] - m * A[i, k]

            A[k, k] = -sigma
        
    return A, beta

def apply(A, beta, b):
    A = np.array(A, dtype = float, copy = True)
    b = np.array(b, dtype = float, copy = True)

    m = A.shape[0]
    s = len(beta)

    for k in range(s) :
        if beta[k] == 0 :
            continue

        dot = beta[k] * b[k]
        for i in range (k + 1, m) :
            dot += A[i, k] * b[i]

        m = dot / beta[k]

        b[k] -= m * beta[k]
        for i in range (k + 1, m) :
            b[i] -= m * A[i, k]

    return b

def utris(R, b, error = 1e-12) :
    n = R.shape[0]
    x = np.zeros(n)

    for i in range (n - 1, -1, -1) :
        if(abs(R[i, i]) < error) :
            raise ValueError("Element diagonal nul")
        
        s = 0.0
        for j in range (i + 1, n) :
            s += R[i, j] * x[j]

        x[i] = (b[i] - s) / R[i, i]

    return x

def CMMP(A, b) :
    A_1, beta = algorithm(A)
    y = apply(A_1, beta, b)

    n = A.shape[1]
    R = A_1[:n, :n]
    y_2 = y[:n]

    x = utris(R, y_2)
    return x


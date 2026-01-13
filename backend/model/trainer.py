from .solver import least_squares_svd

def train_xg_model(X, y):
    return least_squares_svd(X, y)
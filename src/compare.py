import numpy as np
from model import load_data, build_design_matrix, build_target_vector
from alg import solve_least_squares

def train_model(data_path="../data/shots.csv", save_path="../data/beta.npy"):
    df = load_data(data_path)

    A = build_design_matrix(df)
    y = build_target_vector(df)

    beta = solve_least_squares(A, y)

    np.save(save_path, beta)

    print("Model antrenat cu succes!")
    print("Coeficienți beta:")
    print(beta)

    return beta

if __name__ == "__main__":
    train_model()
import numpy as np
from model import load_data, build_design_matrix, build_target_vector
from alg import solve_least_squares

def train_model(data_path="data/shots.csv", save_path="data/beta.npy"):
    # 1. Încărcăm datele
    df = load_data(data_path)

    # 2. Construim matricea A și vectorul y
    A = build_design_matrix(df)
    y = build_target_vector(df)

    # 3. Antrenăm modelul folosind QR cu reflectori
    beta = solve_least_squares(A, y)

    # 4. Salvăm coeficienții
    np.save(save_path, beta)

    print("Model antrenat cu succes!")
    print("Coeficienți beta:")
    print(beta)

    return beta


if __name__ == "__main__":
    train_model()
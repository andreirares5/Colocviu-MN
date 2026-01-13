import numpy as np
import pandas as pd

def load_data(path):
    """
    Încarcă dataset-ul shots.csv și returnează un DataFrame.
    """
    return pd.read_csv(path)


def build_design_matrix(df):
    """
    Construiește matricea A pentru modelul xG:
    A = [1, d, angle, body_part, d^2, angle^2]
    """
    d = df["distance"].values
    angle = df["angle"].values
    b = df["body_part"].values

    A = np.column_stack([
        np.ones_like(d),   # termenul liber
        d,
        angle,
        b,
        d**2,
        angle**2
    ])

    return A


def build_target_vector(df):
    """
    Vectorul țintă y = goal (0 sau 1).
    """
    return df["goal"].values


def predict(beta, distance, angle, body_part):
    """
    Calculează xG pentru un singur șut folosind coeficienții beta.
    """
    x = np.array([
        1,
        distance,
        angle,
        body_part,
        distance**2,
        angle**2
    ])

    return float(np.dot(x, beta))
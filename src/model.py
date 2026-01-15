import numpy as np
import pandas as pd

def load_data(path):
    return pd.read_csv(path)


def build_design_matrix(df):
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
    return df["xg"].values



def predict(beta, distance, angle, body_part):
    x = np.array([
        1,
        distance,
        angle,
        body_part,
        distance**2,
        angle**2
    ])

    return float(np.dot(x, beta))
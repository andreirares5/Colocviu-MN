import pandas as pd
import numpy as np
import os

def load_dataset():
    """
    Încarcă dataset-ul pentru antrenarea modelului xG.
    CSV-ul trebuie să conțină coloanele:
    distance, angle, goal
    """

    # directorul curent al acestui fișier
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # mergem două nivele în sus: model/ -> backend/ -> proiect/
    project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))

    # construim calea completă către data/shots.csv
    csv_path = os.path.join(project_root, "data", "shots.csv")

    # citim CSV-ul
    df = pd.read_csv(csv_path)

    # X = [1, distance, angle]
    X = df[["distance", "angle"]].values
    X = np.hstack([np.ones((X.shape[0], 1)), X])  # bias

    # y = goal (0/1)
    y = df["goal"].values

    return X, y
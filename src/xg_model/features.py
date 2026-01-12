import numpy as np
import pandas as pd

def load_data(csv_path) :
    data = pd.read_csv(csv_path)

    distances = data["distance"].values
    angles = data["angle"].values
    goals = data["goals"].values

    return distances, angles, goals

def build_matrtix(distances, angles) :
    m = len(distances)
    ones = np.ones(m)

    A = np.column_stack((ones, distances, angles))
    return A

def build_target(goals) :
    return np.array(goals, dtype = float)

def load_features(csv_path) :
    distances, angles, goals = load_data(csv_path)
    A = build_matrtix(distances, angles)
    y = build_target(goals)

    return A, y


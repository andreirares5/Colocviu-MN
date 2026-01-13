import numpy as np

def extract_features(shot):
    dist = float(shot["distance"])
    angle = float(shot["angle"])
    return np.array([1, dist, angle])  # bias + 2 features
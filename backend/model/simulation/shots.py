import random

def is_goal(xg):
    """
    Decide dacă este gol pe baza probabilității xG.
    xg este între 0 și 1.
    Returnează True dacă este gol, False altfel.
    """
    return random.random() < xg
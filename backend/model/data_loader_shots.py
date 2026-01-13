import pandas as pd
import os

def load_shots_csv(filename="shots.csv"):
    """
    Încarcă șuturile reale dintr-un fișier CSV.
    CSV-ul trebuie să conțină coloanele:
    team, distance, angle

    Returnează:
    - teamA: listă de șuturi ale echipei A
    - teamB: listă de șuturi ale echipei B
    """

    # directorul curent al acestui fișier
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # mergem două nivele în sus: model/ -> backend/ -> proiect/
    project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))

    # construim calea completă către data/<filename>
    csv_path = os.path.join(project_root, "data", filename)

    # citim CSV-ul
    df = pd.read_csv(csv_path)

    teamA = []
    teamB = []

    # parcurgem fiecare rând
    for _, row in df.iterrows():
        shot = {
            "distance": float(row["distance"]),
            "angle": float(row["angle"])
        }

        if str(row["team"]).strip().upper() == "A":
            teamA.append(shot)
        else:
            teamB.append(shot)

    return teamA, teamB
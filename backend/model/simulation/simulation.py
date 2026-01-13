from model.features import extract_features
from model.predictor import predict_xg
from model.simulation.shots import is_goal
from model.simulation.events import create_event

def simulate_match(w, teamA_shots, teamB_shots):
    """
    Simulează un meci pe baza șuturilor celor două echipe și a vectorului de greutăți w.

    Parametri:
    - w: vectorul de greutăți al modelului xG
    - teamA_shots: listă de dict-uri: {"distance": ..., "angle": ...}
    - teamB_shots: listă de dict-uri: {"distance": ..., "angle": ...}

    Returnează:
    - goals_A: goluri marcate de echipa A
    - goals_B: goluri marcate de echipa B
    - xg_A: xG total al echipei A
    - xg_B: xG total al echipei B
    - events: listă de evenimente (timeline)
    """

    goals_A = 0
    goals_B = 0

    xg_A = 0.0
    xg_B = 0.0

    events = []

    # Echipa A
    for shot in teamA_shots:
        x = extract_features(shot)
        xg = predict_xg(w, x)

        xg_A += xg

        if is_goal(xg):
            goals_A += 1
            outcome = "goal"
        else:
            outcome = "no_goal"

        events.append(
            create_event(
                "A",
                shot["distance"],
                shot["angle"],
                xg,
                outcome,
                xg_A,
                xg_B
            )
        )

    # Echipa B
    for shot in teamB_shots:
        x = extract_features(shot)
        xg = predict_xg(w, x)

        xg_B += xg

        if is_goal(xg):
            goals_B += 1
            outcome = "goal"
        else:
            outcome = "no_goal"

        events.append(
            create_event(
                "B",
                shot["distance"],
                shot["angle"],
                xg,
                outcome,
                xg_A,
                xg_B
            )
        )

    return goals_A, goals_B, xg_A, xg_B, events
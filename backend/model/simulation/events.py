def create_event(team, distance, angle, xg, outcome, xg_A, xg_B):
    """
    Creează un eveniment de șut pentru timeline-ul meciului.

    Parametri:
    - team: "A" sau "B"
    - distance: distanța șutului
    - angle: unghiul șutului
    - xg: xG-ul șutului curent
    - outcome: "goal" sau "no_goal"
    - xg_A: xG total al echipei A după acest șut
    - xg_B: xG total al echipei B după acest șut
    """
    return {
        "team": team,
        "distance": float(distance),
        "angle": float(angle),
        "xg": float(xg),
        "outcome": outcome,
        "xg_total_A": float(xg_A),
        "xg_total_B": float(xg_B)
    }
from flask import Flask, request, jsonify, render_template

from model.data_loader import load_dataset
from model.trainer import train_xg_model
from model.predictor import predict_xg
from model.features import extract_features
from model.simulation.shots import is_goal  # dacă vrei să expui ceva legat de shot-uri
from model.simulation.simulation import simulate_match
from model.data_loader_shots import load_shots_csv


app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Load dataset and train model once at startup
X, y = load_dataset()
w = train_xg_model(X, y)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    x = extract_features(data)
    xg = predict_xg(w, x)
    return jsonify({"xg": float(xg)})


@app.route("/shot", methods=["POST"])
def shot():
    data = request.json

    x = extract_features(data)
    xg = predict_xg(w, x)

    # folosim is_goal(xg) dacă vrei doar goal/no_goal
    outcome = "goal" if is_goal(xg) else "no_goal"

    return jsonify({
        "xg": float(xg),
        "outcome": outcome
    })


@app.route("/simulate_match", methods=["POST"])
def simulate_match_endpoint():
    data = request.json

    teamA = data.get("teamA", [])
    teamB = data.get("teamB", [])

    goals_A, goals_B, xg_A, xg_B, events = simulate_match(w, teamA, teamB)

    return jsonify({
        "simulated_score": f"{goals_A} - {goals_B}",
        "goals_A": goals_A,
        "goals_B": goals_B,
        "xg_A": float(xg_A),
        "xg_B": float(xg_B),
        "events": events
    })


@app.route("/simulate_from_csv", methods=["POST"])
def simulate_from_csv():
    """
    Body JSON: {"filename": "shots.csv"}
    CSV-ul trebuie să fie în folderul data/, cu coloane:
    team,distance,angle
    """
    filename = request.json.get("filename", "shots.csv")

    teamA, teamB = load_shots_csv(filename)

    goals_A, goals_B, xg_A, xg_B, events = simulate_match(w, teamA, teamB)

    return jsonify({
        "simulated_score": f"{goals_A} - {goals_B}",
        "goals_A": goals_A,
        "goals_B": goals_B,
        "xg_A": float(xg_A),
        "xg_B": float(xg_B),
        "events": events
    })


if __name__ == "__main__":
    app.run(debug=True)
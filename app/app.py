from flask import Flask, render_template, request
import numpy as np
import sys
import os

# Adăugăm ../src în sys.path ca să putem importa model.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "src"))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

sys.path.append(SRC_DIR)

from model import predict  # funcția ta de predicție

app = Flask(__name__)

# Încărcăm coeficienții o singură dată, la start
BETA_PATH = os.path.join(DATA_DIR, "beta.npy")
beta = np.load(BETA_PATH)


@app.route("/", methods=["GET", "POST"])
def index():
    xg_value = None
    error = None

    if request.method == "POST":
        try:
            distance = float(request.form.get("distance"))
            angle = float(request.form.get("angle"))
            body_part_str = request.form.get("body_part")

            if distance < 0 or distance > 52.5:
                raise ValueError("Distanța trebuie să fie între 0 și 52.5 metri")
            # Mapăm string -> 0/1
            if body_part_str == "foot":
                body_part = 0
            elif body_part_str == "head":
                body_part = 1
            else:
                raise ValueError("Parte a corpului necunoscută")

            xg_value = predict(beta, distance, angle, body_part)
            xg_value = max(0.0, min(1.0, xg_value))  # clamp în [0,1]

        except Exception as e:
            error = f"Eroare la citirea datelor: {e}"

    return render_template("index.html", xg_value=xg_value, error=error)


if __name__ == "__main__":
    app.run(debug=True)

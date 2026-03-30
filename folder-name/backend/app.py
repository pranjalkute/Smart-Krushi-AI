from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load ML model (if available)
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None

@app.route("/")
def home():
    return "Smart Krushi API Running"

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json

    # Check if ML inputs are present
    if all(k in data for k in ["N", "P", "K", "temp", "humidity", "ph", "rainfall"]) and model:
        # ML Prediction
        features = np.array([[ 
            float(data["N"]), float(data["P"]), float(data["K"]),
            float(data["temp"]), float(data["humidity"]),
            float(data["ph"]), float(data["rainfall"])
        ]])

        prediction = model.predict(features)

        return jsonify({
            "type": "ML Model",
            "crops": [prediction[0]]
        })

    else:
        # Rule-based fallback
        season = data.get("season", "").lower()
        soil = data.get("soil", "").lower()

        if season == "monsoon" and soil == "black":
            crops = ["Cotton", "Soybean"]
        elif season == "winter":
            crops = ["Wheat", "Mustard"]
        else:
            crops = ["Maize", "Pulses"]

        return jsonify({
            "type": "Rule-based",
            "crops": crops
        })

if __name__ == "__main__":
    app.run(debug=True)

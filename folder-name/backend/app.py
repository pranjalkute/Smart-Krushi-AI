from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Home route (for testing)
@app.route("/")
def home():
    return "🌾 Smart Krushi API Running"

# Crop recommendation route
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    try:
        # Extract values (you can improve this later with real inputs)
        # For now using dummy/default mapping
        location = data.get("location", "")
        soil = data.get("soil", "")
        season = data.get("season", "")

        # Dummy values (replace later with real sensor/API data)
        N = 90
        P = 40
        K = 40
        temperature = 25
        humidity = 80
        ph = 6.5
        rainfall = 200

        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        prediction = model.predict(features)

        return jsonify({
            "crops": [prediction[0]]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

# IMPORTANT for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Smart Krushi API Running"

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    
    location = data.get("location", "")
    soil = data.get("soil", "")
    season = data.get("season", "").lower()

    if season == "monsoon":
        crops = ["Rice", "Soybean", "Cotton"]
    elif season == "winter":
        crops = ["Wheat", "Mustard"]
    else:
        crops = ["Maize", "Pulses"]

    return jsonify({
        "crops": crops,
        "message": f"Best crops for {location} with {soil}"
    })

if __name__ == "__main__":
    app.run(debug=True)

import React, { useState } from "react";

export default function App() {
  const [location, setLocation] = useState("");
  const [soil, setSoil] = useState("");
  const [season, setSeason] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ location, soil, season }),
      });

      const data = await response.json();
      setResult("🌾 Recommended Crops: " + data.crops.join(", "));
    } catch (error) {
      setResult("❌ Error connecting to server");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-100 to-green-50 flex items-center justify-center p-6">
      <div className="bg-white shadow-2xl rounded-2xl p-8 w-full max-w-md">
        <h1 className="text-3xl font-bold text-green-700 mb-2 text-center">
          🌾 Smart Krushi
        </h1>
        <p className="text-gray-500 text-center mb-6">
          AI Farming Advisor
        </p>

        <input
          type="text"
          placeholder="📍 Enter Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          className="w-full p-3 border rounded-lg mb-3 focus:outline-none focus:ring-2 focus:ring-green-400"
        />

        <input
          type="text"
          placeholder="🌱 Soil Type (e.g. Black Soil)"
          value={soil}
          onChange={(e) => setSoil(e.target.value)}
          className="w-full p-3 border rounded-lg mb-3 focus:outline-none focus:ring-2 focus:ring-green-400"
        />

        <input
          type="text"
          placeholder="☁️ Season (e.g. Monsoon)"
          value={season}
          onChange={(e) => setSeason(e.target.value)}
          className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-green-400"
        />

        <button
          onClick={handleSubmit}
          className="w-full bg-green-600 text-white p-3 rounded-lg hover:bg-green-700 transition duration-200"
        >
          {loading ? "Analyzing..." : "Get Recommendation"}
        </button>

        {result && (
          <div className="mt-5 p-4 bg-green-100 rounded-lg text-center">
            <p className="text-green-800 font-medium">{result}</p>
          </div>
        )}
      </div>
    </div>
  );
}


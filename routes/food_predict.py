from flask import Blueprint, request, jsonify
import numpy as np
import joblib
import os

food_predict_bp = Blueprint('food_predict', __name__)

# Load model and encoder
MODEL_PATH = "models/know_your_food_model.pkl"
ENCODER_PATH = "models/label_encoder.pkl"

try:
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
except Exception as e:
    model = None
    encoder = None

@food_predict_bp.route("/predict", methods=["POST"])
def predict_food():
    if model is None or encoder is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json()

    try:
        features = np.array([[data["energy_kj"], data["energy_kcal"],
                              data["carb_g"], data["protein_g"],
                              data["fat_g"], data["freesugar_g"]]])

        prediction = model.predict(features)
        food_name = encoder.inverse_transform(prediction)[0]

        return jsonify({"predicted_food_name": food_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

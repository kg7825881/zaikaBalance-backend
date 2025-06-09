from flask import Blueprint, request, jsonify
import joblib
import numpy as np
import os

nutrient_tracker_bp = Blueprint('nutrient_tracker', __name__)

model_path = os.path.join("models", "nutrient_tracker_model.pkl")
encoder_path = os.path.join("models", "nutrient_tracker_label_encoder.pkl")

try:
    model = joblib.load(model_path)
    label_encoder = joblib.load(encoder_path)
except Exception as e:
    model = None
    label_encoder = None

@nutrient_tracker_bp.route('/predict-nutrient-status', methods=['POST'])
def predict_nutrient_status():
    if model is None or label_encoder is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.json
    try:
        features = np.array([[
            data['energy_kcal'],
            data['carb_g'],
            data['protein_g'],
            data['fat_g'],
            data['freesugar_g']
        ]])
        pred_encoded = model.predict(features)
        pred_label = label_encoder.inverse_transform(pred_encoded)[0]

        return jsonify({"nutrient_status": pred_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

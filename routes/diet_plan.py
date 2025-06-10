from flask import Blueprint, request, jsonify
import numpy as np
import joblib

diet_planner_bp = Blueprint('diet_planner', __name__)

# Load model and encoder once
nn_model = joblib.load('models/diet_planner_model.pkl')
label_encoder = joblib.load('models/diet_planner_label_encoder.pkl')

@diet_planner_bp.route('/recommend', methods=['POST'])
def recommend_meals():
    data = request.json
    try:
        features = np.array([[ 
            data['energy_kj'], 
            data['energy_kcal'], 
            data['carb_g'], 
            data['protein_g'], 
            data['fat_g'], 
            data['freesugar_g']
        ]])
        
        distances, indices = nn_model.kneighbors(features)
        
        # Find top 5 closest meals
        recommended_indices = indices[0]
        recommended_meals = label_encoder.inverse_transform(recommended_indices)
        
        return jsonify({
            'recommended_meals': recommended_meals.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

from flask import Blueprint, request, jsonify

bmi_bp = Blueprint('bmi', __name__)

@bmi_bp.route('/calculate', methods=['POST'])
def calculate_bmi():
    data = request.json
    height = data.get('height')  # in cm
    weight = data.get('weight')  # in kg
    if not height or not weight:
        return jsonify({'message': 'Height and weight required'}), 400

    try:
        height_m = float(height) / 100
        weight_kg = float(weight)
        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 2)
        category = ''
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 25:
            category = 'Normal weight'
        elif 25 <= bmi < 30:
            category = 'Overweight'
        else:
            category = 'Obese'
        return jsonify({'bmi': bmi, 'category': category})
    except:
        return jsonify({'message': 'Invalid height or weight'}), 400

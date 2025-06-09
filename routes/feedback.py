from flask import Blueprint, request, jsonify
from utils.auth_helper import token_required
import json
import os

feedback_bp = Blueprint('feedback', __name__)
FEEDBACK_FILE = 'data/feedback.json'

def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []
    with open(FEEDBACK_FILE, 'r') as f:
        return json.load(f)

def save_feedback(feedback_list):
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(feedback_list, f, indent=4)

@feedback_bp.route('/submit', methods=['POST'])
@token_required
def submit_feedback(current_user):
    data = request.json
    feedback_list = load_feedback()
    entry = {'user': current_user, 'feedback': data.get('feedback')}
    feedback_list.append(entry)
    save_feedback(feedback_list)
    return jsonify({'message': 'Feedback submitted'})

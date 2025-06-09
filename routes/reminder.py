from flask import Blueprint, request, jsonify
from utils.auth_helper import token_required
import json
import os

reminder_bp = Blueprint('reminder', __name__)
REMINDER_FILE = 'data/reminders.json'

def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return {}
    with open(REMINDER_FILE, 'r') as f:
        return json.load(f)

def save_reminders(reminders):
    with open(REMINDER_FILE, 'w') as f:
        json.dump(reminders, f, indent=4)

@reminder_bp.route('/set', methods=['POST'])
@token_required
def set_reminder(current_user):
    data = request.json
    reminders = load_reminders()
    if current_user not in reminders:
        reminders[current_user] = []
    reminders[current_user].append(data)
    save_reminders(reminders)
    return jsonify({'message': 'Reminder set'})

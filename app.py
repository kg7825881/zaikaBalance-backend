from flask import Flask
from flask_cors import CORS

from routes.auth import auth_bp
from routes.bmi import bmi_bp
from routes.feedback import feedback_bp
from routes.food_predict import food_predict_bp
from routes.nutrient_tracker import nutrient_tracker_bp
from routes.reminder import reminder_bp
from routes.recipes import recipes_bp
from routes.diet_plan import diet_planner_bp  # ✅ Correctly imported

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(bmi_bp, url_prefix='/bmi')
    app.register_blueprint(feedback_bp, url_prefix='/feedback')
    app.register_blueprint(food_predict_bp, url_prefix='/food')
    app.register_blueprint(nutrient_tracker_bp, url_prefix='/tracker')
    app.register_blueprint(reminder_bp, url_prefix='/reminder')
    app.register_blueprint(recipes_bp, url_prefix='/recipes')
    app.register_blueprint(diet_planner_bp, url_prefix='/diet')  # ✅ Corrected name

    return app

# ✅ Needed for Gunicorn
app = create_app()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')


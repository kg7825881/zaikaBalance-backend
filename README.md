# 🥗 Zaika Balance – Smart Diet Recommendation App

Zaika Balance is a smart web application designed to help users manage their diet and nutrition efficiently. It combines machine learning with Indian food datasets to provide personalized diet plans, nutrient tracking, and food analysis.

🚀 Features
🔍 Know Your Food – Predicts calories & nutrients from Indian dish names.

🧠 Smart Diet Planner – Recommends diet plans based on user profile.

📊 Nutrient Tracker – Tracks and compares daily nutrient intake.

📏 BMI Calculator – Calculates Body Mass Index.

🍱 Recipe Book – Curated recipes for 5 user categories (Gymrat, 9-5, Pregnancy, etc.)

⏰ Food Reminder – Customizable reminders for meals.

🧾 Feedback Widget – Collects user feedback to improve the app.

🧠 Tech Stack
Frontend: Next.js (hosted on Vercel)

Backend: Flask (hosted on Render)

Database: JSON & Flat Files (extendable to MongoDB or Firebase)

Machine Learning: Scikit-learn, TensorFlow

Other Libraries: Pandas, NumPy, Matplotlib

📁 Folder Structure
arduino
Copy
Edit
zaika-balance-backend/
├── app.py
├── config.py
├── requirements.txt
├── routes/
│   ├── auth.py
│   ├── bmi.py
│   ├── diet_plan.py
│   ├── diet_planner.py
│   ├── feedback.py
│   ├── food_predict.py
│   ├── nutrient_tracker.py
│   ├── profile.py
│   ├── reminder.py
│   └── recipes.py
├── models/
│   ├── know_your_food.py
│   ├── track_your_nutrients.py
│   ├── diet_planner_model.py
│   └── anuvaad_dataset.csv
└── utils/
    └── helpers.py
⚙️ Setup Instructions
Clone the Repository

bash
Copy
Edit
git clone https://github.com/dinosauronthemoon/zaika-balance-backend
cd zaika-balance-backend
Create Virtual Environment

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Train Models

bash
Copy
Edit
python models/know_your_food.py
python models/track_your_nutrients.py
python models/diet_planner_model.py
Run the App

bash
Copy
Edit
python app.py

📌 API Endpoints (Sample)
Feature	Endpoint
Predict Dish Nutrients	POST /food/predict
Generate Diet Plan	POST /dietplanner/generate
Track Nutrients	POST /tracker/track
Calculate BMI	POST /bmi/calculate

👩‍💻 Made with ❤️ #   z a i k a B a l a n c e - b a c k e n d 
 
 

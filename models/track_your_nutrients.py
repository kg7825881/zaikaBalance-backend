import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

print("🚀 Nutrient Tracker Model Training Started")

data_path = os.path.join("models", "anuvaad_dataset.csv")
df = pd.read_csv(data_path, encoding="ISO-8859-1")

# Columns available (based on your earlier info):
# food_code, food_name, primarysource, energy_kj, energy_kcal, carb_g, protein_g, fat_g, freesugar_g

# Define thresholds for Ideal / Excess / Deficient for each nutrient (example values):
thresholds = {
    'energy_kcal': (50, 250),     # Ideal between 50 and 250 kcal per serving
    'carb_g': (10, 50),           # Ideal between 10 and 50 g carbs
    'protein_g': (5, 20),         # Ideal between 5 and 20 g protein
    'fat_g': (3, 15),             # Ideal between 3 and 15 g fat
    'freesugar_g': (0, 10)        # Ideal less than 10 g free sugar
}

# Function to classify each nutrient value
def classify_nutrient(value, nutrient):
    low, high = thresholds[nutrient]
    if value < low:
        return 'Deficient'
    elif value > high:
        return 'Excess'
    else:
        return 'Ideal'

# Create a target column by combining nutrient statuses
def combined_status(row):
    statuses = [classify_nutrient(row[n], n) for n in thresholds.keys()]
    # If any nutrient is Excess, overall is Excess; else if any Deficient, overall Deficient; else Ideal
    if 'Excess' in statuses:
        return 'Excess'
    elif 'Deficient' in statuses:
        return 'Deficient'
    else:
        return 'Ideal'

# Add combined target column
df['nutrient_status'] = df.apply(combined_status, axis=1)

# Features and target
X = df[['energy_kcal', 'carb_g', 'protein_g', 'fat_g', 'freesugar_g']]
y = df['nutrient_status']

# Encode target labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))

# Save model and label encoder
model_path = os.path.join("models", "nutrient_tracker_model.pkl")
encoder_path = os.path.join("models", "nutrient_tracker_label_encoder.pkl")

joblib.dump(model, model_path)
joblib.dump(le, encoder_path)

print(f"Model saved to {model_path}")
print(f"Label encoder saved to {encoder_path}")

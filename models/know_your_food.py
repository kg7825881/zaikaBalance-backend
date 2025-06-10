# models/know_your_food.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import os

print("🚀 Script started")

# Define the CSV file path
data_path = os.path.join("models", "anuvaad_dataset.csv")
print(f"📄 Loading dataset from {data_path}")

# Load the dataset
df = pd.read_csv(data_path, encoding='ISO-8859-1')  # or encoding='latin1'

# Drop rows with missing values in essential columns
df.dropna(subset=['food_name', 'energy_kj', 'energy_kcal', 'carb_g', 'protein_g', 'fat_g', 'freesugar_g'], inplace=True)

print("✅ Dataset loaded and cleaned!")

# Feature columns and target
features = ['energy_kj', 'energy_kcal', 'carb_g', 'protein_g', 'fat_g', 'freesugar_g']
target = 'food_name'

X = df[features]
y = df[target]

# Encode target labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Test Accuracy: {test_accuracy:.2f}")

# Save model and encoder with compression
model_path = os.path.join("models", "know_your_food_model.pkl.gz")
encoder_path = os.path.join("models", "label_encoder.pkl.gz")

joblib.dump(model, model_path, compress=3)
joblib.dump(encoder, encoder_path, compress=3)

print(f"💾 Compressed model saved to: {model_path}")
print(f"💾 Compressed encoder saved to: {encoder_path}")
print("✅ All done!")






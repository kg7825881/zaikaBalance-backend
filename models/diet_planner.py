import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
import joblib

print("🚀 Starting Diet Planner model training...")

data_path = "models/anuvaad_dataset.csv"
df = pd.read_csv(data_path, encoding='ISO-8859-1')

# Select features and target
features = ['energy_kj', 'energy_kcal', 'carb_g', 'protein_g', 'fat_g', 'freesugar_g']
target = 'food_name'

# Clean dataset: drop rows with missing values in features or target
df = df.dropna(subset=features + [target])

# Features matrix
X = df[features].values

# Target labels
y = df[target].values

# Label encode food names (optional, if you want to keep numeric form)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Use NearestNeighbors for meal recommendation based on nutrient input
nn_model = NearestNeighbors(n_neighbors=5, algorithm='auto')
nn_model.fit(X)

# Save model and label encoder
joblib.dump(nn_model, 'models/diet_planner_nn_model.pkl')
joblib.dump(le, 'models/diet_planner_label_encoder.pkl')

print("✅ Diet Planner model trained and saved!")

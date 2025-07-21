import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("data/goa_beach_safety_dataset.csv")  # Make sure the path is correct

# Encode labels
encoders = {}
for col in ['Beach', 'Weather', 'Crowd_Level', 'Tide', 'Hazard', 'Safety']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features and labels
X = df[['Beach', 'Weather', 'Crowd_Level', 'Tide', 'Hazard']]
y = df['Safety']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "beach_safety_model.pkl")
joblib.dump(encoders, "label_encoders.pkl")

print("✅ Model and encoders saved successfully!")

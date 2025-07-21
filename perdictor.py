import joblib
import numpy as np

# === Load the trained model and encoders ===
try:
    model = joblib.load("model/beach_safety_model.pkl")
    encoders = joblib.load("model/label_encoders.pkl")

    # 🔍 DEBUG: Show all valid classes for each encoder
    for key in encoders:
        print(f"✅ Valid {key} classes: {encoders[key].classes_}")

except FileNotFoundError:
    print("❌ ERROR: Model or encoder file not found. Make sure both .pkl files are in the 'model/' folder.")
    exit()

# === Encode user input using the same encoders used during training ===
def encode_input(beach, weather, crowd, tide, hazard):
    # Validate inputs
    for label, value in zip(
        ['Beach', 'Weather', 'Crowd_Level', 'Tide', 'Hazard'],
        [beach, weather, crowd, tide, hazard]
    ):
        valid_classes = encoders[label].classes_
        if value not in valid_classes:
            print(f"❌ ERROR: '{value}' not found in valid {label} options: {list(valid_classes)}")
            exit()

    return np.array([
        encoders['Beach'].transform([beach])[0],
        encoders['Weather'].transform([weather])[0],
        encoders['Crowd_Level'].transform([crowd])[0],
        encoders['Tide'].transform([tide])[0],
        encoders['Hazard'].transform([hazard])[0]
    ]).reshape(1, -1)

# === Predict beach safety ===
def predict_safety(beach, weather, crowd, tide, hazard):
    features = encode_input(beach, weather, crowd, tide, hazard)
    result = model.predict(features)[0]
    label = encoders['Safety'].inverse_transform([result])[0]
    return label

# === Test the function ===
if __name__ == "__main__":
    # ✅ Update these values only with those seen in encoder classes
    beach = "Baga"
    weather = "Sunny"
    crowd = "High"
    tide = "High"
    hazard = "Glass"  # Must exactly match label encoder values

    prediction = predict_safety(beach, weather, crowd, tide, hazard)
    print(f"\n🏖️ {beach} beach is currently predicted to be: {prediction}")

# 🏖️ Goa Beach Safety Monitor - AI Project Documentation

## 📘 Table of Contents

1. Introduction
2. Problem Statement
3. Project Objectives
4. SDG Alignment
5. System Overview
6. Dataset Creation
7. Machine Learning Model
8. System Architecture
9. APIs and External Services
10. Features
11. Technical Stack
12. Screenshots
13. Output Interpretation
14. Future Scope
15. Conclusion
16. References

---

## 1. Introduction

The Goa Beach Safety Monitor is an AI-powered Streamlit web application designed to predict real-time safety levels of popular beaches in Goa, India. It integrates live weather and tide data with machine learning to generate safety recommendations and assist tourists, locals, and safety personnel.

---

## 2. Problem Statement

Beachgoers in Goa are often exposed to uncertain conditions due to unpredictable weather, tides, and crowd density. The absence of a centralized, intelligent advisory system can lead to unsafe swimming, crowd congestion, or inadequate planning.

---

## 3. Project Objectives

* Develop a smart advisory system for real-time beach safety.
* Integrate AI-based prediction using multiple live data points.
* Visualize safety trends and beach conditions.
* Provide personalized insights using crowd, tide, and weather data.
* Promote sustainable and safe coastal tourism.

---

## 4. SDG Alignment

### ✅ SDG 11: Sustainable Cities & Communities

* Smart city solution for tourism and coastal safety.
* Supports urban resilience and crowd management.

### ✅ SDG 13: Climate Action

* Tracks and interprets climate-driven phenomena like tide and storm surges.
* Enhances awareness and personal responsibility.

---

## 5. System Overview

* **Frontend**: Streamlit dashboard
* **Backend**: Python + trained ML model
* **Data Sources**: OpenWeatherMap API, WorldTides API, custom dataset
* **Prediction Output**: Green (Safe), Yellow (Caution), Red (Danger)

---

## 6. Dataset Creation

* A custom AI-generated dataset was built using simulated beach safety records.
* Fields include: Beach, Weather, Crowd Level, Tide, Hazard, Safety Label
* Saved as `data/goa_beach_safety_dataset.csv`
* Used LabelEncoder to encode categorical features.

---

## 7. Machine Learning Model

* Algorithm: Random Forest Classifier
* Input features: Beach, Weather, Crowd\_Level, Tide, Hazard
* Output: Safety Label
* Accuracy validated using test split
* Serialized using `joblib` into `model/beach_safety_model.pkl`

---

## 8. System Architecture

```
User Input → Live APIs → Encoders → ML Model → Safety Prediction → Visualization & Logs
```

### Key Components:

* `app.py`: Main Streamlit app logic
* `predictor.py`: Predicts safety using model & encoders
* `train_model.py`: Prepares dataset and trains classifier

---

## 9. APIs and External Services

* **OpenWeatherMap API** – For real-time weather per beach
* **WorldTides API** – For tide height & level analysis
* **Botpress Chatbot** – Conversational AI assistant for users

---

## 10. Features

* 🌤 Live Weather Display
* 🌊 Tide Level & 24-Hour Forecast
* 👥 Monsoon-Aware Crowd Prediction
* 📍 Interactive Folium Map
* 📈 Weekly Safety Log Chart
* 🤖 Chatbot Integration (Botpress)

---

## 11. Technical Stack

* **Language**: Python
* **Web Framework**: Streamlit
* **ML**: Scikit-learn (RandomForest)
* **Visualization**: Plotly, Folium
* **Deployment Ready**: Yes (local / Streamlit Cloud)

---

## 12. Screenshots

*(Screenshots folder should include: home, map, tide chart, prediction result, chatbot, trends)*

* `screenshots/mainPage.png`
* `screenshots/Safety Trends.png`
* `screenshots/Tide Forecast (Next 24 Hours).png`
* `screenshots/prediction.png`
* `screenshots/predictionPage.png`
* `screenshots/chatbot.png`
* * `screenshots/mapView.png`

---

## 13. Output Interpretation

* **Green**: Safe for swimming and recreation
* **Yellow**: Caution advised due to crowd, weather, or tides
* **Red**: Dangerous; swimming should be avoided

Each prediction is logged in `logs/safety_log.csv` for future analysis.

---

## 14. Future Scope

* Integration with lifeguard alert systems
* SMS/Email push notifications
* Real-time satellite crowd detection
* Weather anomaly alerts

---

## 15. Conclusion

The Goa Beach Safety Monitor demonstrates how AI and environmental data can be combined to enhance safety, climate resilience, and sustainable tourism. This solution is scalable for other coastal regions and cities.

---

## 16. References

* [OpenWeatherMap API](https://openweathermap.org/api)
* [WorldTides API](https://www.worldtides.info)
* [Streamlit Documentation](https://docs.streamlit.io)
* [Scikit-learn Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

```
```

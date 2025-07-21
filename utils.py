# utils.py

# === Goa Beach Coordinates ===
beach_locations = {
    "Baga": (15.5639, 73.7517),
    "Calangute": (15.5439, 73.7550),
    "Anjuna": (15.5750, 73.7448),
    "Candolim": (15.5166, 73.7622),
    "Palolem": (15.0094, 74.0232),
    "Colva": (15.2789, 73.9220),
    "Miramar": (15.4744, 73.8055),
    "Morjim": (15.6166, 73.7397),
    "Arambol": (15.6865, 73.7040),
    "Vagator": (15.5889, 73.7359)
}

# === Weather Aliases ===
weather_aliases = {
    "clear": "Sunny",
    "clouds": "Cloudy",
    "rain": "Rainy",
    "drizzle": "Rainy",
    "thunderstorm": "Stormy",
    "mist": "Foggy",
    "haze": "Foggy"
}

# === Dummy Tide Function (Replace with real API logic if needed) ===
def fetch_tide_level(beach_name):
    # Add your WorldTides API logic here
    return "Low"  # Dummy return

# === Dummy Weather Function (Replace with real API logic) ===
def fetch_weather(beach_name):
    # Add your OpenWeatherMap API logic here
    return "clear"  # Dummy return

# === Dummy Safety Predictor ===
def predict_safety(beach, weather, crowd, tide, hazard):
    if weather == "Stormy" or tide == "High":
        return "Red"
    elif weather == "Cloudy" or tide == "Medium":
        return "Yellow"
    return "Green"

import streamlit as st
from streamlit_folium import st_folium
import folium

# === Import helper functions & data ===
from utils import (
    fetch_tide_level,
    fetch_weather,
    predict_safety,
    beach_locations,
    weather_aliases
)

st.set_page_config(page_title="Beach Map", layout="wide")
st.title("🗺️ Live Beach Safety Map")

def generate_beach_map():
    m = folium.Map(location=[15.55, 73.77], zoom_start=10)
    
    for beach_name, (lat, lon) in beach_locations.items():
        try:
            tide_level = fetch_tide_level(beach_name)
            weather_live = fetch_weather(beach_name)
            weather = weather_aliases.get(weather_live, "Sunny")
            
            safety = predict_safety(
                beach_name,
                weather,
                "Medium",
                tide_level,
                "None"
            )
            
            icon_color = "red" if safety == "Red" else "orange" if safety == "Yellow" else "green"
            icon = "exclamation-triangle" if safety == "Red" else "exclamation-circle" if safety == "Yellow" else "check-circle"
            
            folium.Marker(
                [lat, lon],
                popup=f"""
                <b>{beach_name}</b><br>
                Status: <b>{safety}</b><br>
                Weather: {weather}<br>
                Tide: {tide_level}
                """,
                tooltip=f"{beach_name}: {safety}",
                icon=folium.Icon(color=icon_color, icon=icon, prefix='fa')
            ).add_to(m)
        except Exception as e:
            st.warning(f"Couldn't process {beach_name}: {str(e)}")
    
    return m

st_folium(generate_beach_map(), width=1200, height=600)

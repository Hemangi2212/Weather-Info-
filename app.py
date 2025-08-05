import streamlit as st
import requests

# Title
st.title("☁️ Weather App")

# Input city name
city = st.text_input("Enter city name:")

# API Key (You can store this in a .env file for security)
API_KEY = "b0ea042b3cfe49c70ffa6467aa72a63a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

if city:
    data = get_weather(city)

    if data.get("cod") == 200:
        st.success(f"Weather in {city.capitalize()}")
        st.write(f"🌡️ Temperature: {data['main']['temp']} °C")
        st.write(f"🌥️ Condition: {data['weather'][0]['description'].title()}")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        st.write(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
    else:
        st.error("City not found. Please try again.")

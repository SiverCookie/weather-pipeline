import requests
import os
from dotenv import load_dotenv 

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Iasi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    if not API_KEY:
        raise RuntimeError("Missing OPENWEATHER_API_KEY environment variable")
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "description": data["weather"][0]["description"]
    }

from src.fetch_data import fetch_weather

def test_fetch_weather_structure():
    data = fetch_weather()
    assert "temperature" in data
    assert "humidity" in data
    assert "pressure" in data
    assert "description" in data


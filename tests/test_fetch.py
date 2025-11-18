from unittest.mock import patch
from src.fetch_data import fetch_weather

@patch("src.fetch_data.requests.get")
def test_fetch_weather_structure(mock_get):
    mock_response = {
        "main": {
            "temp": 20,
            "humidity": 50,
            "pressure": 1013
        },
        "weather": [{"description": "clear sky"}],
    }

    class MockResp:
        def raise_for_status(self):
            pass
        def json(self):
            return mock_response

    mock_get.return_value = MockResp()

    data = fetch_weather()
    assert "temperature" in data
    assert "humidity" in data
    assert "pressure" in data
    assert "description" in data

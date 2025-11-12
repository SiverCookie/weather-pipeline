from src.db import get_connection
from src.fetch_data import fetch_weather

def insert_measurement(values):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO measurements (temperature, humidity, pressure, weather_description)
        VALUES (%s, %s, %s, %s)
        """,
        (values["temperature"], values["humidity"], values["pressure"], values["description"])
    )
    conn.commit()
    cur.close()
    conn.close()

def main():
    weather = fetch_weather()
    insert_measurement(weather)

if __name__ == "__main__":
    main()

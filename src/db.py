# src/db.py
import psycopg

def get_connection():
    return psycopg.connect(
        dbname="weather_data",
        user="weather_user",
        password="0000",
        host="localhost",
        port=5432
    )


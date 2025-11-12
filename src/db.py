# src/db.py
import os
import psycopg

def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME", "weather_data"),
        user=os.getenv("DB_USER", "weather_user"),
        password=os.getenv("DB_PASS", "0000"),
        host=os.getenv("DB_HOST", "localhost"),  # va fi "postgres" pe GitHub Actions
        port=os.getenv("DB_PORT", "5432")
    )

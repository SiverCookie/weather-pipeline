from src.db import get_connection

def test_insert_temp_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CREATE TEMP TABLE temp_measurements (temperature REAL, humidity REAL, pressure REAL, weather_description TEXT)")
    conn.commit()

    cur.execute(
        "INSERT INTO temp_measurements VALUES (%s, %s, %s, %s)",
        (10.0, 50.0, 1015.0, "clear sky")
    )
    conn.commit()

    cur.execute("SELECT * FROM temp_measurements")
    row = cur.fetchone()

    cur.close()
    conn.close()

    assert row == (10.0, 50.0, 1015.0, "clear sky")


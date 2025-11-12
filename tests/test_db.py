from src.db import get_connection

def test_db_connection():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    cur.close()
    conn.close()
    assert result[0] == 1


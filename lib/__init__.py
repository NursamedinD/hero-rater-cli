import sqlite3

DATABASE_FILE = "hero_database.db"
CONN = sqlite3.connect(DATABASE_FILE)
CURSOR = CONN.cursor()

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS heroes (
        id INTEGER PRIMARY KEY,
        name TEXT,
        power TEXT,
        origin TEXT
    )
""")
CONN.commit()




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
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        hero_id INTEGER,
        rating INTEGER,
        FOREIGN KEY (hero_id) REFERENCES heroes (id) ON DELETE CASCADE
    )
""")

CONN.commit()




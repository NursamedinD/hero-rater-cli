import sqlite3

DATABASE_FILE = 'database.db'

CONN = sqlite3.connect(DATABASE_FILE)
CURSOR = CONN.cursor()

def database():
    CURSOR.execute('''
CREATE TABLES IF NOT EXISTS heroes (
                   id INTERGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                   power TEXT NOT NULL
                   origin TEXT NOT NULL
                   )
                   ''')
    CURSOR.execute()
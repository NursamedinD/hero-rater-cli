import sqlite3

DATABASE_FILE = 'database.db'

CONN = sqlite3.connect(DATABASE_FILE)
CURSOR = CONN.cursor()

def database():
    CURSOR.execute('''
CREATE TABLES IF NOT EXISTS heroes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                   power TEXT NOT NULL,
                   origin TEXT NOT NULL
                   )
                   ''')
    
    CURSOR.execute('''
CREATES TABLES IF NOT EXISTS review (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   hero_id INTEGER NOT NULL,
                   rating INTERG NOT NULL CHECK(rating between 1 and 10),
                   FOREIGN KEY (hero_id) refrences heroes(id)
                   )
                   ''')
    
CONN.commit()
CONN.close()
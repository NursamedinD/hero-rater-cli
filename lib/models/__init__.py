import sqlite3

DATABASE_FILE = 'database.db'

CONN = sqlite3.connect(DATABASE_FILE)
CURSOR = CONN.cursor()

def database_init():
    CURSOR.execute('''
CREATE TABLE IF NOT EXISTS heroes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                   power TEXT NOT NULL,
                   origin TEXT NOT NULL
                   )
                ''')
    
    CURSOR.execute('''
CREATE TABLE IF NOT EXISTS review (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   hero_id INTEGER NOT NULL,
                   rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 10),
                   FOREIGN KEY (hero_id) REFERENCES heroes(id) 
                   )
                ''')
    
CONN.commit()

database_init()
import sqlite3
from __init__ import CURSOR, CONN, DATABASE_FILE

class Hero:
    def __init__(self, id, name, power, origin):
        self.id = id
        self.name = name
        self.power = power
        self.origin = origin

    @classmethod
    def add_hero(cls, name, power, origin):
        CONN = sqlite3.connect(DATABASE_FILE)
        CURSOR = CONN.cursor()

        CURSOR.execute(
            "INSERT INTO heroes (name, power, origin) VALUES (?, ?, ?)",
            (name, power, origin)
        )
        CONN.commit()
        print(f"Hero '{name}' added successfully!")

    @classmethod
    def get_all_heroes(cls):
        CURSOR.execute("SELECT * FROM heroes")
        return CURSOR.fetchall()
    
    @classmethod
    def find_by_id(cls):
        CURSOR.execute("SELECT * FROM heroes WHERE id = ?", (hero_id,))
        return CURSOR.fetchone()
    
    @classmethod
    def delete_hero(cls):
        CURSOR.execute("DELETE FROM heroes WHERE id = ?", (hero_id,))
        CONN.commit()
        print(f"Hero with ID {hero_id} has been deleted.")

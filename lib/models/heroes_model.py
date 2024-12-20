import sqlite3
from lib import CURSOR, CONN 


class Hero:
    def __init__(self, id, name, power, origin):  
        self.id = id
        self.name = name
        self.power = power
        self.origin = origin


    @classmethod
    def add_hero(cls, name, power, origin):
        CURSOR.execute(
            "INSERT INTO heroes (name, power, origin) VALUES (?, ?, ?)",
            (name, power, origin)
        )
        CONN.commit()


    @classmethod
    def get_all_heroes(cls):
        CURSOR.execute("SELECT * FROM heroes")
        heroes = CURSOR.fetchall()
        return [cls(hero[0], hero[1], hero[2], hero[3]) for hero in heroes]


    @classmethod
    def find_by_id(cls, hero_id):
        CURSOR.execute("SELECT * FROM heroes WHERE id = ?", (hero_id,))
        hero = CURSOR.fetchone()
        if hero:
            return cls(hero[0], hero[1], hero[2], hero[3])
        return None


    @classmethod
    def delete_hero(cls, hero_id):
        CURSOR.execute("DELETE FROM heroes WHERE id = ?", (hero_id,))
        CONN.commit()


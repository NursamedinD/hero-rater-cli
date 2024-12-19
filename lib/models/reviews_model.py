from __init__ import CONN, CURSOR

class Review:
    def __init__(self, id, hero_id, rating):
        self.id = id
        self.hero_id = hero_id
        self.rating = rating

    @classmethod
    def add_review(cls, hero_id, rating):
        CURSOR.execute(
            "INSERT INTO reviews (hero_id, rating) VALUES (?, ?)",
            (hero_id, rating)
        )
        CONN.commit()
        print(f"Review added successfully for Hero ID {hero_id}.")

    @classmethod
    def get_reviews_for_hero(cls, hero_id):
        CURSOR.execute("SELECT * FROM reviews WHERE hero_id = ?", (hero_id,))
        return CURSOR.fetchall()
    
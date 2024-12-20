import sqlite3
from lib import CONN, CURSOR

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
        review_data = CURSOR.fetchall()  
        reviews = []
        for review in review_data:
            review_obj = cls(
                id=review[0],        
                hero_id=review[1],   
                rating=review[2]     
            )
            reviews.append(review_obj)
        return reviews
    
    @classmethod
    def delete_review(cls, review_id):
        CURSOR.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
        CONN.commit()
        (f"Review with ID {review_id} has been deleted.")


    
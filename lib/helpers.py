# lib/helpers.py

def check_rating(rating):
    if rating.isdigit():
        rating = int(rating)
        return 1 <= rating <= 10
    return False
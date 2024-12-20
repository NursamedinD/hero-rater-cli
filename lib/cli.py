# lib/cli.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models.heroes_model import Hero
from lib.models.reviews_model import Review
from lib.helpers import check_rating


def main_menu():
    print("\n <--- Hero Rater CLI --->")
    print("1. Add a new hero")
    print("2. View Heroes list")
    print("3. Add a review for a hero")
    print("4. View all reviews for heroes")
    print("5. Delete a Hero")
    print("6. Delete a Review")
    print("7. Exit")
    return input("Type (1-7) to choose an option: ")

def add_hero():
    print("\n -- Add a new Hero --")
    name = input("Enter hero name here: ")
    power = input("Enter hero's main power here: ")
    origin = input("Enter hero's origin: ")
    Hero.add_hero(name, power, origin)
    print(f"Hero '{name} has been added successfully!")

def view_heroes():
    print("\n <- All Heroes ->")
    heroes = Hero.get_all_heroes()
    if heroes:
        for hero in heroes:
            print(
                f"ID: {hero.id}, Name: {hero.name}, Power: {hero.power}, Origin: {hero.origin}"
            )
    else:
        print("No Heroes found.")

def add_reviews():
    print("\n -- Add a Review for a Hero --")
    hero_id = input("Enter the Hero's ID: ")
    rating = input("Enter a rating (1-10): ")
    if check_rating(rating):
        Review.add_review(hero_id, int(rating))
        print(f"Review added for Hero ID {hero_id} with rating {rating}!")
    else:
        print("Invalid rating. Please enter a number between 1 and 10")

def view_reviews():
    print("\n <- View all Reviews for a Hero")
    hero_id = input("Enter Hero's ID: ")
    reviews = Review.get_reviews_for_hero(hero_id)
    if reviews:
        print(f"Reviews for Hero ID {hero_id}:")
        for review in reviews:
            print(f"Rating: {review.rating}")
    else:
        print(f"No reviews found for Hero ID {hero_id}.")

def delete_hero():
    print("\n --Delete a Hero")
    print("\nCurrent Heroes:")
    heroes = Hero.get_all_heroes()
    for hero in heroes:
        print(f"ID: {hero.id}, Name: {hero.name}, Power: {hero.power}, Origin: {hero.origin}")
    
    hero_id = input("\nEnter Hero ID to delete: ")
    hero = Hero.find_by_id(hero_id)
    
    if hero:
        Hero.delete_hero(hero_id)
        print(f"Hero with ID {hero_id} has been deleted.")
    else:
        print(f"No Hero found with ID {hero_id}")

def delete_review():
    print("\n -- Delete a Review --")
    hero_id = input("Enter Hero ID to see their reviews: ")
    reviews = Review.get_reviews_for_hero(hero_id)
    if reviews:
        print(f"\n Reviews for Hero ID {hero_id}:")
        for review in reviews:
            print(f"Review ID: {review.id}, Rating: {review.rating}")
        review_id = input("\nEnter Review ID to delete: ")
        Review.delete_review(review_id)
    else:
        print(f"No reviews found for Hero ID {hero_id}")


def hero_cli():
    while True:
        choice = main_menu()
        if choice == "1":
            add_hero()
        elif choice == "2":
            view_heroes()
        elif choice == "3":
            add_reviews()
        elif choice == "4":
            view_reviews()
        elif choice == "5":
            delete_hero()
        elif choice == "6":
            delete_review()
        elif choice == "7":
            print("Exiting...see you next time!")
            break
        else:
            print("Invalid Choice. Please select a valid option.")


if __name__ == "__main__":
    hero_cli()

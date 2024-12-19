# lib/cli.py

from lib.models.heroes_model import Hero
from lib.models.reviews_model import Review

def main_menu():
    print("\n <--- Hero Rater CLI --->")
    print("1. Add a new hero")
    print("2. View Heroes list")
    print("3. Add a review for a hero")
    print("4. View all reviews for heroes")
    print("5. Exit")
    return input("Type (1-5) to choose an option: ")

def add_hero():
    print("\n Add a new Hero")
    name = input("Enter hero name here: ")
    power = input("Enter hero's main power here: ")
    origin = input("Enter hero's origin: ")
    Hero.add_hero(name, power, origin)
    print(f"Hero '{name} has been added successfully!")


# def main():
#     while True:
#         choice = main_menu
        





if __name__ == "__main__":
    main()

## Hero Rater CLI

A simple rating app for superheroes and the like, by Nursamedin Abdi Dualle.

# Features
- The ability to add new Heroes.
- The ability to add a rating between 1 and 10 for a hero.
- Delete Heroes you no longer want.
- Delete Reviews you no longer want.

## How to use

# Run locally

You will need a:
- A laptop or computer.
- Stable internet.
- A web browser.

For the cloning process:
- VS Code.
- Ubuntu.
- Understanding of Python, Sqlite.

# Installation process

1. Clone this repo by typing this or even copying and pasting it into your terminal:

`git clone git@github.com:NursamedinD/hero-rater-cli.git`

2. Find the directory of this file by typing:

`cd hero-rater-cli`

3. Open it in VS Code, or your prefered code editor and run these commands:

`pipenv install`
`pipenv shell`

Note: this will allow you test it in your local environment.

## Running the CLI

To run the CLI, type into your terminal in VS code:

`python3 lib/cli.py`

Here I will explain what each option does:

# 1. Add a new Hero

By pressing "1" and then Enter you will be prompted with the following:

- "Enter hero name here: ", here you can enter the name of your desired Hero, for example, Spiderman, Blue Beetle, Black Panther, etc.

- "Enter hero's main power here: ", here you can enter the name of youe hero's power, whether its super strength, flight, or super speed, etc.

- "Enter hero's origin: ", here you can enter the name of the place your hero originates from, this can be a world their come from, or their hometown.

One done you will be told your Hero has been added successfully

# 2. View Heroes List

By pressing "2" and then Enter, you will be show a list (depending how many heroes you have added) which will display:

- Their ID
- Their Name
- Their Power
- Their Origin

# 3. Add a review for a hero

By pressing "3" and then Enter, you will be given the ability to give your hero a rating out of 10, to do so you first need to:

- Press 2 and then Enter first in order to see the Hero and their ID.
- Press 3 and then Enter to add a review.
- Enter the ID of your desired Hero you want to rate.
- You are then prompted to enter a rating of 1 (being the lowest) and 10 (being the highest), also note you can only put in a rating of in between 1 or 10 or else the CLI wont accept it.

# 4. View all reviews for heroes

By pressing "4" and then Enter, you can view the review you have entered for your desired hero, to do so:
- Remember the ID of your desired hero (if you need reminding, make sure to pick option 2 before going into option 4)
- Enter the ID of the hero you want and you will see the rating displayed above the options

# 5. Delete a Hero

By pressing "5" and then Enter, you can delete the hero you no longer want, to do so:
- Press "5" and then Enter, your heroes will then be listed as well as showing you the ID of all heroes
- Enter the ID of the hero based off the ID given and then hit Enter
- To check if it has been removed, press option 2 and it should say "No Heroes found"

# 6. Delete a Review

By pressing "6" and then Enter, you can delete the rating you have given your hero, to do so:
- Press "6" and then Enter
- If needed, refer back to the ID of your Hero that you deleted (See 5)
- A review ID will be displayed for the selected hero ID you chose, type it into the prompt "Enter Review ID to delete: "
- To check if it worked, enter "4" and then press Enter to view all reviews, type in the Hero's ID and see if the review has been cleared

# 7. Exit

By pressing "7" and then Enter you will be taken out of the CLI returning you to your terminal

## Techonologies used

- Python
- Sqlite

# Support

If you run into issues you can reach me at: nursamedin.a.dualle@gmail.com

# License

Copyright © 2024 Nursamedin Abdi Dualle

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
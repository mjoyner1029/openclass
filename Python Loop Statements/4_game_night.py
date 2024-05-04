# task 1
import random

Kitchen = "knives", "pans", "food", "fridge", "stove", "sink"
guesses = 0
option = random.choice(Kitchen)

while True:
    guess = str(input(f"Name something in the kitchen {Kitchen}: "))
    guesses =+ 1

    if guess != option:
        print("Sorry that was inncorrect, please try agin!")
    else:
        print("you were correct!")
        break
    


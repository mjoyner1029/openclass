#task 1
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(f"we suggest you book {venue}")

media = "an audio system" if attendees > 100 else "a projector"
print(f"we suggest you have {media}")

food_choice = input("what kind of catering would you like? vegetarian/non vegetarian: ")
types = "Veggie Delight Caterers" if food_choice == "vegetarian" else "Gourmet Meals Caterers"
print(f"to eat {types} would be good")
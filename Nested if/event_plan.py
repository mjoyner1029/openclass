#task 1
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

media = "an audio system" if attendees > 100 else "aprojector"
print("It is suggested to also add {media}")

food_choice = input("what kind of catering would you like? vegetarian/non vegetarian: ")
types = "Veggie Delight Caterers" if food_choice == "vegetarian" else "Gourmet Meals Caterers"
print(types)
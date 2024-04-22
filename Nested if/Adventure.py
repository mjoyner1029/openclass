# task 1
place = input("Choose a place: forest or cave?: ")

if place == "forest":
    if place == "forest ":
        pass
    action = input("climb a tree or cross a river?: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    if place == "cave ":
        pass
    action2 = input("light a torch or proceed in the dark?: ")
    if action2 == "proceed in the dark":
        print("you are lost in the dark")
    elif action2 == "light a torch":
        print("You find a hidden treasure!")

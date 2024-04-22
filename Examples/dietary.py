meal_type = input("do you prefer veg or non-veg")
dietary = input("do you want sugar-free or regular")

if meal_type == "veg":
    if dietary == "sugar-free":
        print("fruit salad")
    else:
        print("veg cake")
else:
    if dietary == "sugar-free":
        print("sugar free ice cream")
    else:
        print("chocolate cake")
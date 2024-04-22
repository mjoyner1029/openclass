mood = input("how are you feeling today? (happy/sad/adventurous):")
weather = input("what's the weather like? (sunny/rainy):")

if mood == "happy":
    if weather == "sunny":
        print("comedy")
    else:
        print("romanitic")
elif mood == "sad":
    print("drama")
else:
    print("adventure")
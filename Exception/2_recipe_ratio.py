# task 1
import math

print('Welcome to the recipe ratio adjuster!')
# we need to figure out the number of servings
desired_servings = float(input('What is the number of people you are servings? '))
original_servings = float(input('How many people does the recipe say it feeds? '))
ingredients = float(input('What are the ingredients? '))

def get_servings():
    try:
        original_servings = int(input("Enter the original number of servings: "))
        desired_servings = int(input("Enter the desired number of servings: "))
        return original_servings, desired_servings
    except ValueError:
        print("Please enter valid numbers.")
        return None, None

def get_ingredients(original_servings):
    ingredients = {}
    try:
        num_ingredients = int(input("Enter the number of ingredients: "))
        for _ in range(num_ingredients):
            ingredient = input("Enter the name of the ingredient: ")
            quantity = float(input(f"Enter the quantity of {ingredient} for {original_servings} servings: "))
            ingredients[ingredient] = quantity
        return ingredients
    except ValueError:
        print("Please enter valid numbers.")
        return None

def calculate_new_quantities(original_servings, desired_servings, ingredients):
    ratio = desired_servings / original_servings
    new_quantities = {ingredient: quantity * ratio for ingredient, quantity in ingredients.items()}
    return new_quantities

def display_new_quantities(desired_servings, new_quantities):
    print("\nNew ingredient quantities for", desired_servings, "servings:")
    for ingredient, quantity in new_quantities.items():
        print(f"{ingredient}: {quantity:.2f}")

def main():
    original_servings, desired_servings = get_servings()
    if original_servings is None or desired_servings is None:
        return

    ingredients = get_ingredients(original_servings)
    if ingredients is None:
        return

    new_quantities = calculate_new_quantities(original_servings, desired_servings, ingredients)
    display_new_quantities(desired_servings, new_quantities)

if __name__ == "__main__":
    main()
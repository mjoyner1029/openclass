# task 1
import math

#fahrenheit = input('Welcome to your weather forcaster: + /n please enter your tempature in fahrenheit: ')

def fahrenheit_to_celsius(fahrenheit):
    try:
        # Attempt to convert the input to a float
        fahrenheit = float(fahrenheit)
    except ValueError:
        # If conversion fails, print an error message
        print('Please enter a valid number.')
        return
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5 / 9
    
    # Print the temperature in Celsius rounded to 3 decimal places
    print("Temperature in Celsius:", round(celsius, 2))

# Get input from the user
try:
    user_input = input("Enter temperature in Fahrenheit: ")
    fahrenheit = float(user_input)
except ValueError:
    print("Please enter a valid number.")
else:
    fahrenheit_to_celsius(fahrenheit)

finally:
    print('Thank you for using the weather forecast application!')
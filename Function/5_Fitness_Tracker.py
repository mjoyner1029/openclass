# task 1
activities = ['Dancing', 'Swimming', 'Biking']
duration = [10, 20, 15]

def fitness_tracker(activities, duration):
    print(f'today you were {activities} for {duration} minutes. ')

fitness_tracker('Dancing', '10')
fitness_tracker('swimming', '20')
fitness_tracker('biking', '15')

import math

def multiplication(duration, burn):
    return(duration * burn) 

duration = int(input('input your workout duration: '))
burn = 3.5

calories = print(duration,'*', burn , '=', 
      multiplication(duration, burn))

print(f"Your total calorie burn for the day was{calories}")
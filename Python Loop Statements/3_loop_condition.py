# task 1
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# task 2
import random

Moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for day in days_of_week:
    if day == "Tuesday":
        break
    for mood in Moods:
        mood = random.choice(Moods)
    print(f"On " + (day) + ", you were feeling " + mood + ": " )
# task 1

import random

Moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for day in days_of_week:
    for mood in Moods:
        mood = random.choice(Moods)
    print(f"On " + (day) + ", you were feeling " + mood + ": " )
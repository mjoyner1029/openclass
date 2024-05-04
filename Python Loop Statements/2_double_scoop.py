import random

Moods = ["Happy", "Sad", "Energetic", "Calm"]
time_of_day = ["morning" , "afternoon", "night"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

mood = random.choice(Moods)

for day in days_of_week:
    for time in time_of_day:
        for mood in Moods:
            mood = random.choice(Moods)
        print(f"On " + (day) +  " " + (time) + ", you were feeling " + mood + ": " )
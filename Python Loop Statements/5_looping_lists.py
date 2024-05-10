# task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
count = 0


for genre in genres:
    count += 1
    if genre == "Jazz":
        print(f"{count} Jazz from the city of New Orleans")
    if genre == "Rock":
        print(f"{count} Rock and roll baby!")
    if genre == "Hip-hop":
        print(f"{count} All the MC's stand up!")
    if genre == "Classical":
        print(f"{count} Relax to some classical music")

# task 2 while 
count = 0

while True:
    genre = genres[count]
    count += 1
    if genre == "Jazz":
        print(f"{count} Jazz from the city of New Orleans")
    elif genre == "Rock":
        print(f"{count} Rock and roll baby!")
    elif genre == "Classical":
        print(f"{count} Relax to some classical music")
    else:
        break
print("All the MC's stand up!")
        

# task 3
for i in range(len(genres)):
    if genres[i] != "Classical":
        print(f"Genre {genres[i]} is suitable for the light show!")
    else:
        print(f"{genres[i]} is so boring it doesnt need lights")
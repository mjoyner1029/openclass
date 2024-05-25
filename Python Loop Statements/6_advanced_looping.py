# task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for i in range(len(genres)):
    if genres[i] == "Rock":
        print(f"tracks 2 {genres[i]}")
    elif genres[i] == "Classical":
        print(f"tracks 4 {genres[i]}")


# task 2
genres.append("Music")
print(genres)

# task 3
count_down = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(len(count_down)):
    if count_down[i] == 0:
        print(f"{count_down[::-1]}The beat drops now!")

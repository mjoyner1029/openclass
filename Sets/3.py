# Given list of artist names with potential duplicates
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

# Initialize an empty set for unique artists
unique_artists = set()

# Iterate through the list of artist names and add to the set
for artist in artist_names:
    unique_artists.add(artist)

# Check for duplicates
duplicate_found = len(unique_artists) != len(artist_names)

# Display the result
if duplicate_found:
    print("Duplicate artists found: True")
else:
    print("Duplicate artists found: False")

# Print the unique set of artists
print("Unique artists:", unique_artists)
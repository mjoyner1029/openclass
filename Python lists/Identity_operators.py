# task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

intersected_list = []

for element in submitted:

  if element in attended:

      intersected_list.append(element)

print(intersected_list)

# task 2
print(submitted is attended)

# task 3
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended.remove = ("Eve")
attended.remove = ("frank")
print(attended)
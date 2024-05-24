# task 1
grocery_list = []
removed_items = []  # To store removed items

needs_items = True

while needs_items:
    item_to_add = input("What item do you want to add? ")
    grocery_list.append(item_to_add)
    print("Your grocery list has the following items in it:")
    print("-----")
    for item in grocery_list:
        print("- " + item)
    print("-----")

    answer = input("Add another item? (y/n) ")
    if answer.lower() == "n":
        needs_items = False

print("Your final grocery list is:")
print("-----")
for item in grocery_list:
    print("- " + item)
print("-----")

# Allow removal of items
remove_items = input("Do you want to remove any items? (y/n) ")
if remove_items.lower() == "y":
    while True:
        item_to_remove = input("Enter the item you want to remove: ")
        if item_to_remove in grocery_list:
            removed_items.append(item_to_remove)  # Add to removed items list
            grocery_list.remove(item_to_remove)
            print(item_to_remove + " has been removed from the list.")
        else:
            print("Item not found in the list.")
        another_removal = input("Do you want to remove another item? (y/n) ")
        if another_removal.lower() != "y":
            break

print("Your updated grocery list is:")
print("-----")
for item in grocery_list:
    print("- " + item)
print("-----")

# Print removed items
print("Items removed:")
print("-----")
for item in removed_items:
    print("- " + item)
print("-----")
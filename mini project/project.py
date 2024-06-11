def print_todo_list(todo_list):
    """Print the current to-do list"""
    print("Your to-do list has the following tasks in it:")
    print("-----")
    for item in todo_list:
        completion_status = "completed" if item["completed"] else "pending"
        print(f"- {item['task']} ({completion_status})")
    print("-----")

def add_task(todo_list):
    """Add a task to the to-do list"""
    item_to_add = input("What task do you want to add? ")
    todo_list.append({"task": item_to_add, "completed": False})
    print_todo_list(todo_list)

def remove_task(todo_list):
    """Remove a task from the to-do list"""
    removed_items = []
    while True:
        item_to_remove = input("Enter the item you want to remove: ")
        found = False
        for i, item in enumerate(todo_list):
            if item["task"] == item_to_remove:
                removed_items.append(item["task"])
                del todo_list[i]
                found = True
                print(item_to_remove + " has been removed from the list.")
                break
        if not found:
            print("Item not found in the list.")
        another_removal = input("Do you want to remove another item? (y/n) ")
        if another_removal.lower() != "y":
            break
    print_todo_list(todo_list)

def mark_task_complete(todo_list):
    """Mark a task as completed"""
    while True:
        task_to_complete = input("Enter the task you completed: ")
        found = False
        for item in todo_list:
            if item["task"] == task_to_complete:
                item["completed"] = True
                found = True
                print(task_to_complete + " marked as complete!")
                break
        if not found:
            print("Item not found in the list.")
        another_completion = input("Mark another task complete? (y/n) ")
        if another_completion.lower() != "y":
            break
    print_todo_list(todo_list)

def main():
    """Main function for the To-Do List App"""
    print('Welcome to the To-Do List App!')

    todo_list = []

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Print the to-do list")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            mark_task_complete(todo_list)
        elif choice == "4":
            print_todo_list(todo_list)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
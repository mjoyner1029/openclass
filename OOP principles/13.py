class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget
    
    # Getter and setter for category name
    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_name):
        self.__category_name = new_name
    
    # Getter and setter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
            # Adjust remaining budget if necessary
            if self.__remaining_budget > new_budget:
                self.__remaining_budget = new_budget
        else:
            print("Error: Budget must be a positive number.")
    
    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"${amount} added to {self.__category_name} expenses.")
            else:
                print("Error: Insufficient budget.")
        else:
            print("Error: Expense amount must be a positive number.")
    
    # Method to display budget category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")

def add_new_category(categories):
    category_name = input("Enter category name: ")
    allocated_budget = float(input("Enter allocated budget: "))
    new_category = BudgetCategory(category_name, allocated_budget)
    categories.append(new_category)
    print("Category added successfully!")

def set_category_budget(categories):
    category_name = input("Enter category name: ")
    new_budget = float(input("Enter new budget: "))
    category = next((cat for cat in categories if cat.get_category_name() == category_name), None)
    if category:
        category.set_allocated_budget(new_budget)
        print("Budget updated successfully!")
    else:
        print("Category not found!")

def add_category_expense(categories):
    category_name = input("Enter category name: ")
    amount = float(input("Enter expense amount: "))
    category = next((cat for cat in categories if cat.get_category_name() == category_name), None)
    if category:
        category.add_expense(amount)
    else:
        print("Category not found!")

def display_category_summary(categories):
    category_name = input("Enter category name: ")
    category = next((cat for cat in categories if cat.get_category_name() == category_name), None)
    if category:
        category.display_category_summary()
    else:
        print("Category not found!")

def display_all_categories(categories):
    for category in categories:
        category.display_category_summary()

def main():
    categories = []
    while True:
        print("\nBudget Management System")
        print("1. Add a new category")
        print("2. Set category budget")
        print("3. Add an expense to a category")
        print("4. Display category summary")
        print("5. Display all categories")
        print("6. Quit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_new_category(categories)
        elif choice == '2':
            set_category_budget(categories)
        elif choice == '3':
            add_category_expense(categories)
        elif choice == '4':
            display_category_summary(categories)
        elif choice == '5':
            display_all_categories(categories)
        elif choice == '6':
            print("Thank you for using the Budget Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
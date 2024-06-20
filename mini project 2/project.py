import os
import re

contacts = {}

def add_contact():
    # Implementation to add a new contact
    name = input('Enter the contacts first and last name: ')
    phone_num = input('Enter the contacts phone number: ')
    email = input('Enter the contacts email: ')
    addition_info = input('Is there any other info for this contact ')
    
    contacts[name] = {'phone': phone_num, 'email': email}
    print(f"Contact {name} added successfully.")

def edit_contact():
    # Implementation to edit an existing contact
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.") 

def delete_contact():
    # Implementation to delete a contact
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")


def search_contact():
    # Implementation to search for a contact
    name = input("Enter the name of the contact you want to search for: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def display_all_contacts():
    # Implementation to display all contacts
    if contacts: 
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

def export_contacts_to_file():
    # Implementation to export contacts to a text file
    filename = input("Enter the filename to export contacts to: ")
    with open(filename, 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")
    print(f"Contacts exported to {filename} successfully.")

def import_contacts_from_file():
    # Implementation to import contacts from a text file
    filename = input("Enter the filename to import contacts from: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts[name] = {'phone': phone, 'email': email}
        print(f"Contacts imported from {filename} successfully.")
    else:
        print("File not found.")

def main():
    print("Welcome to the Contact Management System!")
    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file (BONUS)")
        print("8. Quit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts_to_file()
        elif choice == '7':
            import_contacts_from_file()
        elif choice == '8':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
class Book:
    def __init__(self, title, author, ISBN, publication_date):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.availability_status = "Available"
    
    def borrow_book(self):
        if self.availability_status == "Available":
            self.availability_status = "Borrowed"
            return True
        else:
            return False
    
    def return_book(self):
        self.availability_status = "Available"
    
    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Published: {self.publication_date}, Status: {self.availability_status}"

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book.title)
            return True
        else:
            return False
    
    def return_book(self, book):
        book.return_book()
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
    
    def display_details(self):
        return f"Name: {self.name}, Library ID: {self.library_id}, Borrowed Books: {', '.join(self.borrowed_books)}"

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
    
    def display_details(self):
        return f"Author: {self.name}, Biography: {self.biography}"
    
class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
    
    def display_details(self):
        return f"Genre: {self.name}, Description: {self.description}, Category: {self.category}"

books = []
users = []
authors = []
genres = []

def main():
    print("Welcome to the Library Management System!")
    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            book_operations_menu()
        elif choice == '2':
            user_operations_menu()
        elif choice == '3':
            author_operations_menu()
        elif choice == '4':
            genre_operations_menu()
        elif choice == '5':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

def book_operations_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            ISBN = input("Enter book ISBN: ")
            publication_date = input("Enter book publication date: ")
            new_book = Book(title, author, ISBN, publication_date)
            books.append(new_book)
            print("Book added successfully!")
        elif choice == '2':
            user_name = input("Enter user name: ")
            book_title = input("Enter book title to borrow: ")
            user = next((user for user in users if user.name == user_name), None)
            book = next((book for book in books if book.title == book_title), None)
            if user and book and user.borrow_book(book):
                print("Book borrowed successfully!")
            else:
                print("Borrowing failed. Please check the user name or book title.")
        elif choice == '3':
            user_name = input("Enter user name: ")
            book_title = input("Enter book title to return: ")
            user = next((user for user in users if user.name == user_name), None)
            book = next((book for book in books if book.title == book_title), None)
            if user and book:
                user.return_book(book)
                print("Book returned successfully!")
            else:
                print("Returning failed. Please check the user name or book title.")
        elif choice == '4':
            search_title = input("Enter book title to search: ")
            found_books = [book.display_details() for book in books if search_title.lower() in book.title.lower()]
            if found_books:
                for book_detail in found_books:
                    print(book_detail)
            else:
                print("No books found with the given title.")
        elif choice == '5':
            for book in books:
                print(book.display_details())
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

def user_operations_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter user library ID: ")
            new_user = User(name, library_id)
            users.append(new_user)
            print("User added successfully!")
        elif choice == '2':
            user_name = input("Enter user name to view details: ")
            user = next((user for user in users if user.name == user_name), None)
            if user:
                print(user.display_details())
            else:
                print("User not found.")
        elif choice == '3':
            for user in users:
                print(user.display_details())
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def author_operations_menu():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            new_author = Author(name, biography)
            authors.append(new_author)
            print("Author added successfully!")
        elif choice == '2':
            author_name = input("Enter author name to view details: ")
            author = next((author for author in authors if author.name == author_name), None)
            if author:
                print(author.display_details())
            else:
                print("Author not found.")
        elif choice == '3':
            for author in authors:
                print(author.display_details())
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def genre_operations_menu():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter genre name: ")
            description = input("Enter genre description: ")
            category = input("Enter genre category: ")
            new_genre = Genre(name, description, category)
            genres.append(new_genre)
            print("Genre added successfully!")
        elif choice == '2':
            genre_name = input("Enter genre name to view details: ")
            genre = next((genre for genre in genres if genre.name == genre_name), None)
            if genre:
                print(genre.display_details())
            else:
                print("Genre not found.")
        elif choice == '3':
            for genre in genres:
                print(genre.display_details())
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
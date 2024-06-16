# task 1

def library_system(library):
    format_books = []
    for book_name, author in library:
        format_books.append(f"{book_name} written by {author}")
        return "\n".join(format_books)

# Input the number of itineraries
num_books = int(input("Enter the number of books: "))

# Input details for each itinerary
library = []
for _ in range(num_books):
    book_name = input("Enter book name: ")
    author = input("Enter author: ")
    library.append((book_name, author))
# Format and print the output
output = library_system(library)
print(output)
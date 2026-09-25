# Create list of favorite books with titles and authors
books = [
    {"title": "Design Patterns", "author": "Erich Gamma"},
    {"title": "Linux Command Line and Shell Scripting Bible", "author": "Richard Blum"},
    {"title": "Precalculus Demystified", "author": "Rhonda Huettenmueller"},
    {"title": "Linux Pocket Guide", "author": "Daniel J. Barrett"},
    {"title": "Concepts in Programming Languages", "author": "John C. Mitchell"},
]

# Function to return the first three books from the list using list slicing
def get_first_three_books(book_list):
    return book_list[:3]

# Dictionary that represents a very basic student database with name and student id
students = {
    "Alice Allison": "S12345",
    "Bob Bundy": "S23456",
    "Charlie Chaplin": "S34567",
    "Diana Donaldson": "S45678",
}

# Function to look up and return a student's ID from the database dictionary
def get_student_id(database, name):
    return database.get(name, None)

if __name__ == "__main__":
    print(" First Three Books Using List Slicing:")
    sliced_books = get_first_three_books(books)
    for idx, book in enumerate(sliced_books, 1):
        print(f"{idx}. '{book['title']}' by {book['author']}")
    
    print("\nStudent Database:")
    for name, sid in students.items():
        print(f"Student: {name} | ID: {sid}")

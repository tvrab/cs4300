from src.task5 import (
    books, 
    get_first_three_books,
    students,
    get_student_id,
)

# Function to test that the books variable is a list containing book dictionaries with title and author
def test_books_list_structure():

    # Make sure that books is in fact a list
    assert isinstance(books, list)

    # Make sure there are at least three books in the list
    assert len(books) >= 3

    # Iterate through each book dictionary to check for mandatory title and author keys
    for book in books:
        assert "title" in book and "author" in book

# Function that tests that the get_first_three_books uses list slicing to return the first 3 books
def test_first_three_books_slicing():

    # Retrieve the first three books using the function
    first_three = get_first_three_books(books)

    # Verify that the sliced results is exactly three elements
    assert len(first_three) == 3

    # Make sure that the return list matches Python's expected list slice syntax
    assert first_three == books[:3]

# Function that tests that the students data structure is a dictionary mappying students names to ids
def test_student_database_structure():

    # Make sure students is a python dictionary
    assert isinstance(students, dict)

    # Make sure the dictionary is not empty
    assert len(students) > 0

    # Ensure each key is a student name string and each value is a valid ID (string/int)
    for name, student_id in students.items():
        assert isinstance(name, str)
        assert isinstance(student_id, (str, int))

# Function to test looking up student ids from the dictionary for both existing and non-existent students
def test_get_student_id_lookup():

    # Extract the first student's name string and get their id
    first_student_name = list(students.keys())[0]
    expected_id = students[first_student_name]

    # Make sure get_student_id functin returns the correct ID for a valid student
    assert get_student_id(students, first_student_name) == expected_id

    # Make sure that searching for a student not in the database safely returns none
    assert get_student_id(students, "NonExistentStudent") is None
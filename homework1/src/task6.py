import os

# Function to read a text file and return the total word count
def count_words(file_path):
    
    # Read a text file
    with open(file_path, "r", encoding="utf-8") as file:

        # Return the total word count 
        return len(file.read().split())


if __name__ == "__main__":
    
    # Set the path to the task6 read me.txt
    readme_path = "task6_read_me.txt"
    
    # Try to count the words using count words function and print the results
    try:
        total_words = count_words(readme_path)
        print(f"Total word count in '{readme_path}': {total_words}")

    # Handle the file not found error if needed by telling the user there was a problem
    except FileNotFoundError:
        print(f"File '{readme_path}' not found.")
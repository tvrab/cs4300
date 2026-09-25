from src.task3 import check_number, get_first_prime_numbers, sum_of_numbers, is_prime

# Function to test positive numbers with the check_number function
def test_check_number_positive():
    assert check_number(10) == "positive"

# Function to test negative numbers with the check_number function
def test_check_number_negative():
    assert check_number(-100) == "negative"

# Function to test zero with the check_number function
def test_check_number_zero():
    assert check_number(0) == "zero"

# Function to test floats numbers with the check_number function
def test_check_number_floats():
    assert check_number(0.0001) == "positive"
    assert check_number(0.00) == "zero"
    assert check_number(-1.01335) == "negative"

# Function to test the is_prime function
def is_prime():
    
    # Prime numbers to test
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(13) is True

    # Non-Prime numbers to test
    assert is_prime(4) is False
    assert is_prime(100) is False
    assert is_prime(1000) is False

    # Edge cases to test (less than 2)
    assert is_prime(-3) is False
    assert is_prime(0) is False
    assert is_prime(1) is False

# Function to test the get first prime numbers function
def test_get_first_prime_numbers():

    # Create the expected answer as an array
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Get the actual answer using the get_first_prime_numbers function
    result = get_first_prime_numbers()

    # Check to see if it contains 10 items 
    assert len(result) == 10

    # Compare the expected answer to the actual answer
    assert result == expected_primes

# Function to test the sum_of_numbers function
def test_sum_of_numbers():
    
    # Call the function for the first 100 numbers and check the answer to make sure it matches the expected answer
    assert sum_of_numbers(1, 100) == 5050

    



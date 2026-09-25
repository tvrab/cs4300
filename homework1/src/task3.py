# Define a function to check to see if a number is positive, negative, or zero
def check_number(n):

    # If n is greater than 0 it is positive, 
    if n > 0:
        return "positive"

    # If n is less than 0 it is negative
    elif n < 0:
        return "negative"

    # If n is not greater than 0 or less than 0, then it is zero
    else:
        return "zero"

# Define a function that returns true if the number is prime, and false if not
def is_prime(n):

    # Prime numbers start are positive, and 1 is not a prime number
    if n < 2: 
        return False
    
    # Loop through potential divisors from 2 to the square root of n
    # (because that is all that is needed to find all possible divisors)
    for i in range(2, int(n**0.5) + 1):

        # If i evenly divides n, it means i is a factor of n and that means 
        # that n is not a prime number
        if n % i == 0:
            return False

    # If no factors are found, it is a prime number, so return True
    return True

# Define a function to get the first 10 prime numbers (using the helper function is_prime defined above)
def get_first_prime_numbers():
    
    # Declare array to hold the prime numbers
    primes = []

    # Prime numbers start at 2 and the 10th prime number is 29, so used
    # range of 2 to 100 just to have some cushion if needed
    for n in range(2, 100):
        if len(primes) < 10 and is_prime(n):
            primes.append(n)
            
    # Return the array of prime numbers
    return primes

# Define a function to sum the first 100 numbers
def sum_of_numbers(begin=1, end=100):
    
    # Set the total to 0 to begin the summation
    total = 0

    # Set the current index to the beginning (used variable here to make it easier to use this function
    # for other values besides the first 100 numbers)
    current = begin

    # Loop through the values 1-100
    while current <= end:
        
        # Add the value to the total
        total += current

        # Increment the current counter to go to the next value
        current += 1
    
    # Return the calculated total value
    return total
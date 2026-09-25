import numpy as np 
import pytest
from src.task7 import calculate_statistics

# Function to test mean and standard deviation calculation for a basic integer list
def test_calculate_statistics_basic():
    
    # Define a known sample list of integers
    numbers = [10, 20, 30, 40, 50]

    # Use the function with the given sample list
    stats = calculate_statistics(numbers)

    # Check to maker sure the computed mean matches the expected value
    assert stats["mean"] == 30.0

    # Check to make sure the standard deviation matches the approximated value
    assert stats["std"] == pytest.approx(14.1421, rel=1e-3)

# Define a function that tests the statistics calculation with floating-point numbers
def test_calculate_statistics_floats():

    # Define a list containing floating point numbers
    numbers = [1.5, 2.5, 3.5]

    # Use the function with the test numbers
    stats = calculate_statistics(numbers)

    # Check to make sure the mean and standar deviation values match the expected results
    assert stats["mean"] == 2.5
    assert stats["std"] == pytest.approx(0.8164, rel=1e-3)

# Function that tests that passing an empty list will raise a value error
def test_calculate_statistics_empty_list():
    with pytest.raises(ValueError):
        calculate_statistics([])
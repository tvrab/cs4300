import pytest
from src.task4 import calculate_discount

# Function to test the calculate_discount function with integers
def test_discount_integers():
    assert calculate_discount(100, 20) == 80.0

# Function to test the calculate_discount function with floats
def test_discount_floats():
    assert calculate_discount(99.99, 15.0) == pytest.approx(84.9915)

# Function to test the calculate_discount function with mixed data types (int/float and float/int)
def test_discount_mixed_types():
    assert calculate_discount(200, 12.5) == 175.0
    assert calculate_discount(49.50, 10) == pytest.approx(44.55)

# Function to test the calculate_discount function with 0 discount and 100 discount
def test_boundary_discounts():
    assert calculate_discount(50, 0) == 50.0
    assert calculate_discount(50, 100) == 0.0

# Function to test the calculate_discount function with negative prices
def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        calculate_discount(-10, 15)

# Function to test the calculate_discount function with invalid discount amounts
def test_invalid_discount_range_raises_error():
    
    # Test discounts that are too large
    with pytest.raises(ValueError):
        calculate_discount(100, 150)
    
    # Test negative discounts
    with pytest.raises(ValueError):
        calculate_discount(100, -5)

# Function to test the calculate_discount function with invalid datatypes
def test_non_numeric_type_raises_error():
    with pytest.raises(TypeError):
        calculate_discount("100", 20)
        
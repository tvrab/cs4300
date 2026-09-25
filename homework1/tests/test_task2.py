import pytest
from src.task2 import get_integer, get_boolean, get_float, get_string

# Use pytest's paramatrize ability to make the tests easier to group together
# (mostly just trying this because I haven't used it before and wanted to see how it works)
@pytest.mark.parametrize("func, expected_type",
[ 
    (get_boolean, bool),
    (get_float, float),
    (get_integer, int),
    (get_string, str),

])

# Function to test the data types return the expected values
def test_data_types(func, expected_type):
    
    # Get the result of each function
    result = func()

    # Check to make sure that the result matches the expected result type
    assert isinstance(result, expected_type)
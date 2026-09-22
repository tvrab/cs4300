import pytest
from src.task2 import get_integer, get_boolean, get_float, get_string

@pytest.mark.parametrize("func, expected_type",
[ 
    (get_boolean, bool),
    (get_float, float),
    (get_integer, int),
    (get_string, str),

])

def test_data_types(func, expected_type):
    result = func()
    assert isinstance(result, expected_type)
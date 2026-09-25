import os
import pytest
from src.task6 import count_words

# Function to test the count_words function on the task6_read_me.txt file
def test_count_words_readme():
    readme_path = "task6_read_me.txt"
    assert os.path.exists(readme_path), "task6_read_me.txt does not exist!"

    word_count = count_words(readme_path)
    assert isinstance(word_count, int)
    assert word_count > 0

# Function to test count_words function with a temporary test file using pytest's tmp_path fixture
def test_count_words_custom_file(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Hello world! This is a test file with ten words.")

    assert count_words(str(test_file)) == 10

# Function to test count_words function on an empty file
def test_count_words_empty_file(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")

    assert count_words(str(empty_file)) == 0
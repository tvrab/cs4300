```
# CS 4300 - Homework 1: Introduction to Python &amp; Unit Testing

This repository contains the completed source code and unit tests for Homework 1, covering Python fundamentals, virtual environment setup, duck typing, data structures, file I/O, package management, and automated unit testing with `pytest`.

---

## Repository Structure

```

cs4300/ ├── .gitignore ├── homework1/ │ ├── README.md │ ├── task6\_read\_me.txt │ ├── src/ │ │ ├── task1.py │ │ ├── task2.py │ │ ├── task3.py │ │ ├── task4.py │ │ ├── task5.py │ │ ├── task6.py │ │ └── task7.py │ └── tests/ │ ├── test\_task1.py │ ├── test\_task2.py │ ├── test\_task3.py │ ├── test\_task4.py │ ├── test\_task5.py │ ├── test\_task6.py │ └── test\_task7.py └── homework2/

```

---

## Environment &amp; Dependencies

1. **Activate Virtual Environment**:
   ```bash
   source /coursework/hw1_env/bin/activate

```

1. **Install Required Packages**:

```
pip install pytest numpy

```

---

## Task Overview

* **Task 1: Introduction to Python and Testing** (`src/task1.py`, `tests/test_task1.py`) Prints `"Hello, World!"` and uses pytest's `capsys` fixture to verify captured standard output.
* **Task 2: Variables and Data Types** (`src/task2.py`, `tests/test_task2.py`) Demonstrates Python primitive types (int, float, string, bool) with assertions verifying data types.
* **Task 3: Control Structures** (`src/task3.py`, `tests/test_task3.py`) Implements conditional branches (positive/negative/zero), prime number calculations, and a summation loop.
* **Task 4: Functions and Duck Typing** (`src/task4.py`, `tests/test_task4.py`) Implements `calculate_discount` accepting flexible numeric inputs (int and float) with duck typing validation.
* **Task 5: Lists and Dictionaries** (`src/task5.py`, `tests/test_task5.py`) Demonstrates list slicing on book records and safe key lookup on a student database dictionary.
* **Task 6: File Handling** (`src/task6.py`, `tests/test_task6.py`) Reads `task6_read_me.txt` and calculates total word count using context managers.
* **Task 7: Package Management** (`src/task7.py`, `tests/test_task7.py`) Uses the `numpy` package to compute standard deviation and mean on numeric datasets.

---

## Running Code and Unit Tests

To run an individual script:

```
python3 homework1/src/task1.py

```

To run the complete unit test suite across all 7 tasks:

```
python3 -m pytest

```

To run tests for a single task module:

```
python3 -m pytest homework1/tests/test_task7.py

```
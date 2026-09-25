# CS 4300 - Homework 1: Introduction to Python & Unit Testing

This repository contains the completed source code and unit test suite for **Homework 1** in **CS 4300**. The project covers Python language fundamentals, virtual environment setup, duck typing, data structures, file I/O, package management, and automated unit testing with `pytest`.

---

## Repository Layout

```text
cs4300/
├── .gitignore
├── homework1/
│   ├── README.md
│   ├── task6_read_me.txt
│   ├── src/
│   │   ├── task1.py
│   │   ├── task2.py
│   │   ├── task3.py
│   │   ├── task4.py
│   │   ├── task5.py
│   │   ├── task6.py
│   │   └── task7.py
│   └── tests/
│       ├── test_task1.py
│       ├── test_task2.py
│       ├── test_task3.py
│       ├── test_task4.py
│       ├── test_task5.py
│       ├── test_task6.py
│       └── test_task7.py
└── homework2/
```

---

## Environment Setup

1. **Activate Virtual Environment**:
   ```bash
   source /coursework/hw1_env/bin/activate
   ```

2. **Install Required Dependencies**:
   ```bash
   pip install pytest numpy
   ```

---

## Task Overview

| Task | Source File | Test File | Description |
| :--- | :--- | :--- | :--- |
| **Task 1** | `src/task1.py` | `tests/test_task1.py` | Standard console output (`Hello, World!`) with `pytest` `capsys` stdout verification. |
| **Task 2** | `src/task2.py` | `tests/test_task2.py` | Primitive data types (`int`, `float`, `str`, `bool`) and type assertions using `isinstance()`. |
| **Task 3** | `src/task3.py` | `tests/test_task3.py` | Control structures including `if/elif/else` sign checks, a prime number calculator loop, and summation. |
| **Task 4** | `src/task4.py` | `tests/test_task4.py` | Discount calculations demonstrating Python duck typing across integer and floating-point inputs. |
| **Task 5** | `src/task5.py` | `tests/test_task5.py` | Data structures including book list slicing and dictionary lookups for student IDs. |
| **Task 6** | `src/task6.py` | `tests/test_task6.py` | Context managers (`with open`) for reading `task6_read_me.txt` and verifying total word count. |
| **Task 7** | `src/task7.py` | `tests/test_task7.py` | Integration with the third-party `numpy` package to calculate mean and standard deviation. |

---

## Running Unit Tests

To run the complete test suite across all tasks simultaneously:
```bash
python3 -m pytest
```

To run unit tests for a specific task module:
```bash
python3 -m pytest homework1/tests/test_task7.py
```

---

## Submission Checklist

- [x] Environment & repo structure verified (10 pts)
- [x] All 28 unit tests passing across Tasks 1–7 (86 pts)
- [x] Code quality, docstrings, and inline comments included (4 pts)
- [x] Pushed to GitHub repository `cs4300`
- [x] Downloaded `cs4300` folder ready for Canvas submission

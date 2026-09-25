```
# CS 4300 — Homework 1: Introduction to Python &amp; Unit Testing

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&amp;logo=python)
![pytest](https://img.shields.io/badge/pytest-passing-brightgreen?style=flat&amp;logo=pytest)
![Build](https://img.shields.io/badge/tests-28%20passed-success?style=flat)

This repository contains the completed source code and unit test suite for **Homework 1** in **CS 4300**. The project covers Python language fundamentals, virtual environment configuration, duck typing, data structures, file I/O, package management, and automated testing with `pytest`.

---

## 📁 Repository Structure

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

## ⚙️ Environment Setup

1. **Activate the Virtual Environment**:

```
source /coursework/hw1_env/bin/activate

```

1. **Install Required Dependencies**:

```
pip install pytest numpy

```

---

## 📋 Task Summary

| Task       | Module &amp; Test Files                     | Description                                                                                      |
| ---------- | --------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Task 1** | `src/task1.py`<br />`tests/test_task1.py` | Basic console output (`Hello, World!`) with `pytest` `capsys` stdout capture verification.       |
| **Task 2** | `src/task2.py`<br />`tests/test_task2.py` | Primitive data types (`int`, `float`, `str`, `bool`) and type assertions.                        |
| **Task 3** | `src/task3.py`<br />`tests/test_task3.py` | Control structures: `if/elif/else` sign checks, prime number generator loop, and summation.      |
| **Task 4** | `src/task4.py`<br />`tests/test_task4.py` | Product discount calculations demonstrating Python **duck typing** for numeric types.            |
| **Task 5** | `src/task5.py`<br />`tests/test_task5.py` | Data structures: list slicing for book titles/authors and safe dictionary key lookups.           |
| **Task 6** | `src/task6.py`<br />`tests/test_task6.py` | File I/O with context managers (`with open`) and word count verification on `task6_read_me.txt`. |
| **Task 7** | `src/task7.py`<br />`tests/test_task7.py` | Third-party package integration using `numpy` for mean and standard deviation math.              |

---

## 🧪 Running Unit Tests

To run the complete test suite across all tasks simultaneously:

```
python3 -m pytest

```

To run unit tests for an individual task module:

```
python3 -m pytest homework1/tests/test_task7.py
```

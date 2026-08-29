# Moduler_and_Packager

# Multi-Utility Toolkit

A simple Python-based **Multi-Utility Toolkit** that combines different useful operations into one menu-driven console application.

The project demonstrates Python's built-in modules, custom modules, functions, loops, conditional statements, exception handling, and module exploration using `dir()`.

## Features

### 1. Datetime and Time Operations

The toolkit provides several date and time related operations:

* Display current date and time
* Calculate difference between two dates
* Format dates into different formats
* Stopwatch
* Countdown Timer

The program uses Python's `datetime` and `time` modules.

### 2. Mathematical Operations

The Mathematical Operations section provides:

* Factorial calculation
* Compound Interest calculation
* Trigonometric calculations
* Area of geometric shapes

These mathematical functions are handled through the custom `math_utils.py` module.

### 3. Random Data Generation

The project can generate different types of random data:

* Random number
* Random list
* Random password
* Random OTP

The Python `random` module is used for these operations.

### 4. UUID Generation

The toolkit can generate a unique identifier using Python's `uuid` module.

It uses `uuid.uuid4()` to generate a unique UUID.

### 5. File Operations

The project provides basic file management operations:

* Create a new file
* Write to a file
* Read from a file
* Append to a file

These operations are handled through the custom `file_operations.py` module.

### 6. Module Attribute Explorer

The project demonstrates Python's `dir()` function.

The user can enter:

* `math`
* `random`
* `datetime`
* `time`

The program then displays the available attributes and functions of the selected module.

## Project Structure

```text
Multi_Utility_Toolkit
│
├── main.py
│
└── mytools
    │
    ├── __init__.py
    ├── file_operations.py
    └── math_utils.py
```

## Technologies Used

* Python 3
* `datetime`
* `time`
* `math`
* `random`
* `uuid`
* Custom Python modules
* Functions
* Loops
* Conditional Statements
* Exception Handling
* `dir()` function

## Custom Modules

### `math_utils.py`

This module contains the mathematical functions used by the main program, such as:

* Factorial
* Compound Interest
* Trigonometry
* Area calculations

The functions are imported in `main.py` using:

```python
from mytools import math_utils
```

### `file_operations.py`

This module contains the file-related functions:

* `create_file()`
* `write_file()`
* `read_file()`
* `append_file()`

It is imported using:

```python
from mytools import file_operations
```

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### Step 2: Open the Project Folder

Open the terminal or command prompt inside the project folder.

### Step 3: Run the Program

Use:

```bash
python main.py
```

### Step 4: Select an Option

The main menu provides the following options:

```text
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```

The main menu connects all the individual features into one application.

## Example

```text
==========================
Welcome to Multi-Utility Toolkit
==========================

Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit

Enter your choice:
```

## Concepts Demonstrated

This project is useful for practicing several Python concepts:

* Importing built-in modules
* Creating custom modules
* Importing functions from custom packages
* Functions
* `while` loops
* `if-elif-else`
* User input
* Type conversion
* Exception handling
* Date and time handling
* Random data generation
* UUID generation
* File handling
* `dir()` function
* Menu-driven programming
* `if __name__ == "__main__":`

## Program Entry Point

The program starts from the `main()` function when `main.py` is executed directly.

```python
if __name__ == "__main__":
    main()
```

This ensures that the main menu runs when the file is executed directly.

## Purpose of the Project

The main purpose of this project is to create a single console-based toolkit that demonstrates how different Python modules and custom packages can work together in one application.

It is also designed as a practice project for understanding Python modules, packages, functions, and menu-driven programming.

## Future Improvements

Possible future improvements include:

* Add a graphical user interface
* Add more mathematical operations
* Add more file management features
* Add a calculator
* Add unit conversion
* Add better input validation
* Add a logging system
* Add more random data generation options

## Author

**Aashish Gupta**

## License

This project is created for learning and educational purposes.

# OpenSpace Organizer

## Description

OpenSpace Organizer is a Python project designed to organize colleagues into tables and seats inside an open-space office.

The application:

* Reads a list of colleague names from a CSV file
* Randomly distributes colleagues across multiple tables
* Prevents assigning more people than available seats
* Displays the seating arrangement in the terminal
* Stores the final seating plan inside a CSV output file

This project was created to practice:

* Object-Oriented Programming (OOP)
* Python package structure
* File handling
* CSV manipulation
* Modular programming
* Import management
* Randomization logic

---

# Project Structure

```text
challenge-openspace-classifier/
│
├── main.py
├── new_colleagues.csv
├── output.csv
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── openspace.py
│   ├── table.py
│   ├── seat.py
│   └── utils.py
│
├── utils/
│
└── __pycache__/
```

---

# Features

## Read Names from CSV

The application reads colleague names from a CSV file.

Example:

```csv
Anna
Dan
Gaetan
Guillermo
```

---

## Random Seating Assignment

The names are shuffled randomly using Python's `random.shuffle()`.

Each colleague is assigned to:

* a table
* a seat

until all seats are occupied.

---

## Overflow Management

If there are more people than available seats:

* extra people are stored in an overflow list
* they are displayed separately in the terminal

---

## Display Seating Plan

The application displays all occupied seats directly in the console.

Example:

```text
Table 1
- Anna
- Dan

Table 2
- Ibrahim
- Irene
```

---

## Export Results

The final seating arrangement is saved into `output.csv`.

Example:

```csv
Table,Seat,Name
1,1,Anna
1,2,Dan
2,1,Ibrahim
```

---

# Technologies Used

* Python 3
* Object-Oriented Programming
* CSV file handling
* Python modules and packages

---

# Classes Overview

## Seat Class

Represents a single seat.

### Responsibilities

* Store occupant information
* Check if a seat is free
* Assign a person to the seat

---

## Table Class

Represents a table containing multiple seats.

### Responsibilities

* Create seats
* Assign people to available seats
* Check available capacity

---

## OpenSpace Class

Represents the whole office space.

### Responsibilities

* Create multiple tables
* Organize colleagues randomly
* Display seating arrangement
* Save results to CSV

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
```

---

## 2. Enter the project folder

```bash
cd challenge-openspace-classifier
```

---

## 3. Verify Python installation

```bash
python --version
```

Recommended version:

```text
Python 3.10+
```

---

# Usage

## Run the project

From the root project folder:

```bash
python main.py
```

---

# Example Workflow

## Input

`new_colleagues.csv`

```csv
Anna
Dan
Gaetan
Guillermo
```

---

## Execution

```bash
python main.py
```

---

## Console Output

```text
Table 1
- Anna
- Dan

Table 2
- Guillermo
- Gaetan

Overflow: []
```

---

## Generated File

`output.csv`

```csv
Table,Seat,Name
1,1,Anna
1,2,Dan
2,1,Guillermo
2,2,Gaetan
```

---

# Imports and Package Structure

This project uses Python packages.

Example:

```python
from src.openspace import OpenSpace
```

Inside `openspace.py`, relative imports are used:

```python
from .table import Table
```

This ensures compatibility with package execution.

---

# Common Errors and Solutions

## ModuleNotFoundError: No module named 'table'

### Cause

Using:

```python
from table import Table
```

inside a package.

### Solution

Use:

```python
from .table import Table
```

---

## ModuleNotFoundError: No module named 'src'

### Cause

Running the script from the wrong folder.

### Solution

Run the project from the root directory:

```bash
cd challenge-openspace-classifier
python main.py
```

---

# Object-Oriented Programming Concepts Used

This project demonstrates several OOP concepts:

* Classes
* Objects
* Encapsulation
* Composition
* Methods
* Constructors (`__init__`)
* String representation (`__str__`)

---

# Future Improvements

Possible future features:

* GUI interface
* Seat preferences
* Team grouping
* Automatic CSV validation
* Database integration
* Web application version
* Interactive seat visualization

---

# Author

Siegried Camus

---

# License

This project is intended for educational purposes.

# Student Management System

A simple console-based application written in Python to manage student records. The system allows you to add students, update their grades, and display all student information. This project is designed to demonstrate the use of basic Python concepts such as loops, data structures, string manipulation, and functions.

## Table of Contents
- [Features](#features)
- [Concepts Covered](#concepts-covered)
- [Prerequisites](#prerequisites)
- [How to Run the Project](#how-to-run-the-project)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Add Student**: Add a student to the system by entering their ID, name, and grade.
- **Update Student Grade**: Update the grade of an existing student using their ID.
- **Display All Students**: View a list of all students with their IDs, names, and grades.
- **Interactive Menu**: Console-based interactive menu to perform various operations.

## Concepts Covered
- **Loops**: Used for navigating through the menu and iterating over the list of students.
- **Data Structures**: Uses a list of dictionaries to store student information.
- **String Manipulation**: Handles and formats strings for input, display, and search functionality.
- **Functions**: Code modularization using functions to handle specific tasks.

## Prerequisites
- Python 3.x

## How to Run the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/student-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd student-management-system
    ```
3. Run the main script:
    ```bash
    python student_management_system.py
    ```
4. Follow the on-screen prompts to interact with the system.

## Usage
- **Add Student**: Select the option 1 in the menu and provide the student ID, name, and grade.
- **Update Student Grade**: Select the option 2 and enter the student's ID. Then, provide the new grade.
- **Display All Students**: Select option 3 to view the list of all students.
- **Exit**: Select option 4 to exit the program.

## Testing
The project includes test cases to verify its functionality using the `unittest` module. The test cases check the following:
- Adding a student
- Updating a student's grade
- Handling the case when a student ID is not found
- Displaying students
- Handling an empty student list

### Running Tests
1. Make sure you are in the project directory.
2. Run the tests using the following command:
    ```bash
    python -m unittest test_student_management.py
    ```

## Project Structure
```plaintext
student-management-system/
│
├── [student_management_system.py]# Main script with the student management logic
├── [test_student_management.py# Unit tests for the project
└── [README.md]# This README file
1. Project Title
Student Management System Using Python

2. Project Description

The Student Management System is a menu-driven Python application developed to manage student records. It allows users to add student details, view all saved records, search for a student using their ID, and calculate the average marks of all students.
The application stores student information in a text file named students.txt, allowing records to be loaded when the program starts and saved when new students are added. It also displays the current date and time.

This project was developed as part of the Week 6 Python internship final project.

3. Project Objectives

Develop a simple student record management application.
Apply Python programming concepts to a practical problem.
Store and retrieve student information using file handling.
Validate student IDs, names, and marks.
Calculate the average marks of registered students.
Use Git and GitHub to manage and share the project source code.

4. Features

Add Student: Enter a student ID, name, and marks.
Unique Student IDs: Prevent duplicate student IDs.
Input Validation: Check for empty IDs, invalid names, non-numeric marks, and marks outside the range of 0–100.
View All Students: Display the available student records.
Search Student: Find a student using their student ID.
Calculate Average Marks: Calculate the average marks of all available student records.
Date and Time: Display the current date and time.
File Handling: Save student records in students.txt and load them when the application starts.
Menu-Driven Interface: Select operations using a simple numbered menu.
Exit Option: Close the application safely through the menu.

5. Technologies Used
Programming Language: Python
Development Environment: VS Code
Version Control: Git
Code Hosting: GitHub
Data Storage: Text file (students.txt)
Python Module: datetime
6. Python Concepts Implemented

Variables and Data Types: Store student IDs, names, marks, and menu choices.
Input and Output: Use input() and print() to interact with the user.
Operators: Perform comparisons, addition, and division.
Conditional Statements: Use if, elif, and else to control program execution.
Loops: Use for loops to process records and a while loop to keep the menu running.
Functions: Organize the program into reusable functions.
Lists: Store student records in a list.
Dictionaries: Represent each student using fields for ID, name, and marks.
Type Casting: Convert marks to float and the saved marks back to text when writing records.
File Handling: Read student records from and write them to students.txt.
Exception Handling: Handle a missing data file using FileNotFoundError and invalid marks using ValueError.
Modules: Import datetime to display the current date and time.
String Handling: Remove extra whitespace, split records, and format date and time.
Basic Data Validation: Reject empty IDs, duplicate IDs, invalid names, and marks outside the permitted range.
7. Project Workflow

The application starts and loads existing student records from students.txt.
A menu displays the available operations.
The user selects an operation.
For adding a student, the program accepts the ID, name, and marks and validates the input.
Valid student details are added to the list and saved to the text file.
The user can view all student records or search for a student by ID.
The user can calculate average marks or display the current date and time.
The menu continues until the user selects the exit option.
8. Project File Structure

text
## 8. Project File Structure

StudentManagementSystem/
├── main.py
├── README.md
└── screenshots/
    ├── Source_code1.png
    ├── Source_code2.png
    ├── Source_code3.png
    ├── Source_code4.png
    ├── Source_code5.png
    ├── Source_code6.png
    ├── Out_put1.png
    ├── Out_put2.png
    └── Out_put3.png

The `main.py` file contains the application source code. The `README.md` file provides project documentation. The `screenshots/` folder contains screenshots of the source code and program output.
The `students.txt` file is created locally when student records are saved.


9. Installation and Setup

Install Python on your computer.
Install Git.
Clone the GitHub repository or download the project files.
Open the StudentManagementSystem folder in Visual Studio Code.
Ensure that Python is available in your terminal.
10. How to Run the Project

Open a terminal inside the project folder and execute:

bash
python main.py
On Windows, we can also use:
bash
py main.py
Follow the menu instructions to manage student records.

11. Sample Menu

text
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. View All Students
3. Search Student
4. Calculate Average Marks
5. Show Current Date and Time
6. Exit
Enter your choice (1-6):

12. Challenges Faced
The project addresses several practical programming challenges, including validating user input, preventing duplicate student IDs, handling missing files, converting marks into numeric values, and maintaining student records using file handling.

13. Future Improvements
Add options to update and delete student records.
Provide sorting and filtering of student information.
Add a graphical user interface.
Use a database such as SQLite for structured storage.
Generate student performance reports.
Improve handling of names containing commas and more robust file validation.

14. Conclusion
The Student Management System demonstrates the practical use of Python fundamentals, functions, data structures, conditional statements, loops, exception handling, file handling, and the datetime module.

The project provides a simple way to manage student information and calculate average marks. Git and GitHub can be used to track changes and maintain the project repository.

15. GitHub Repository
Repository URL: https://github.com/SHAIK-ABDU-TAYYAB02/StudentManagementSystem.
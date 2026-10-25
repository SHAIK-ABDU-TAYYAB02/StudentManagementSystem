from datetime import datetime

FILE_NAME = "students.txt"

def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    student = {
                        "id": data[0],
                        "name": data[1],
                        "marks": float(data[2])
                    }
                    students.append(student)

    except FileNotFoundError:
        pass

    return students

def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                student["id"] + "," +
                student["name"] + "," +
                str(student["marks"]) + "\n"
            )

    print("Records saved successfully!")

def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter student name: ").strip()

    if not name or "," in name:
        print("Enter a valid name without commas.")
        return

    try:
        marks = float(input("Enter student marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter marks as a number.")
        return

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No student records available.")
        return

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Student Name:", student["name"])
        print("Student Marks:", student["marks"])

def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")

def calculate_average(students):
    if not students:
        print("No records available.")
        return

    total = 0

    for student in students:
        total = total + student["marks"]

    average = total / len(students)
    print("Average marks:", round(average, 2))

def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Show Current Date and Time")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            calculate_average(students)

        elif choice == "5":
            now = datetime.now()
            print("Current date and time:", now.strftime(
                "%d-%m-%Y %H:%M:%S"
            ))

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")

if __name__ == "__main__":
    main()
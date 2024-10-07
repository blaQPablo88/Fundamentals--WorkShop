# Student Management System

# Data structure to hold student information (list of dictionaries)
students = []

# Function to add a new student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")
    
    # Add new student data to the list
    student = {
        'id': student_id,
        'name': name,
        'grade': grade
    }
    students.append(student)
    print(f"Student {name} added successfully!")

# Function to update a student's grade
def update_student_grade():
    student_id = input("Enter Student ID to update: ")
    
    # Search for the student
    for student in students:
        if student['id'] == student_id:
            new_grade = input(f"Enter new grade for {student['name']}: ")
            student['grade'] = new_grade
            print(f"Grade for {student['name']} updated to {new_grade}")
            return
    print("Student not found!")

# Function to display all students
def display_students():
    if not students:
        print("No students to display.")
        return
    
    print("\nStudent List:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")

# Main menu
def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Display All Students")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student_grade()
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main_menu()

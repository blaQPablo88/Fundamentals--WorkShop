# Student Management System

# Data structure to hold student information (list of dictionaries)
# initalize a student variable with an empty list 

# Function to add a new student
def add_student():
    """
    Prompts the user to input student ID, name, and grade, 
    then adds the student to the students list.
    """
    print('\tADDING STUDENT')
    # Get student ID, name, and grade from user input
    # Hint: Use input() to get the values
    id_input = input('create/enter a student number: ')
    name_input = input('enter your name: ')
    grade_input = input('what grade are you in? ')
    
    # Create a dictionary for the student using the input values
    # Example: {'id': student_id, 'name': name, 'grade': grade}
    student = {}
    student['id'] = id_input
    student['name'] = name_input
    student['grade'] = grade_input
    print(student)
    
    # Add the student dictionary to the students list
    # Hint: Use the append() method on the students list
    students = []
    print(len(students))
    if student:
        students.append(student)
        print('Successfully added student')
    else:
        print('Error adding student')
    
    # Print a success message to confirm the student was added

# Function to update a student's grade
def update_student_grade():
    """
    Prompts the user for a student ID, searches for that student in the list, 
    and updates their grade if found.
    """
    # Get the student ID to update from user input
    
    # Loop through the students list to find the student with the given ID
    # Hint: Use a for loop to iterate over students
    
    # If the student is found:
        # Prompt the user for the new grade
        # Update the student's grade in the dictionary
        # Print a success message
    
    # If the student is not found, print an error message

# Function to display all students
def display_students():
    """
    Displays all students in the system, or a message if no students are available.
    """
    # Check if the students list is empty
    # Hint: Use an if statement to check the list's length
    
    # If empty, print "No students to display."
    
    # If not empty, loop through each student in the students list
    # Print the student's ID, name, and grade in a formatted string

# Main menu
def main_menu():
    """
    Displays the main menu and calls the appropriate functions based on user input.
    """
    # while True:
    # Print the menu options
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Student Grade")
    print("3. Display All Students")
    print("4. Exit")
    
    # Get the user's choice using input()
    user_input = input('Select an option: ')
    
    # Use if-elif-else statements to call the appropriate function based on the user's choice
    # Hint: Call add_student(), update_student_grade(), display_students(), or exit the loop
    if user_input.isdigit():
        if user_input == '1':
            add_student()
        elif user_input == '2':
            update_student_grade()
        elif user_input == '3':
            display_students()
        elif user_input == '4':
            exit()
        else:
            while user_input < '1' or user_input > '4':
                user_input = input('Invalid Selection. Select an option (1-4): ')
    else:
        print('Invalid choice')

        
        # If the choice is not between 1 and 4, print an "Invalid choice" message

# Run the program
if __name__ == "__main__":
    main_menu()

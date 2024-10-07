import unittest
from io import StringIO
import sys

# Importing the functions and the students list from the main program
from student_management_system import add_student, update_student_grade, display_students, students

class TestStudentManagementSystem(unittest.TestCase):
    
    def setUp(self):
        # Reset the students list before each test
        global students
        students.clear()

    def test_add_student(self):
        # Simulate user input
        sys.stdin = StringIO('001\nJohn Doe\nA\n')

        # Call the add_student function
        add_student()
        
        # Check if the student was added correctly
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['id'], '001')
        self.assertEqual(students[0]['name'], 'John Doe')
        self.assertEqual(students[0]['grade'], 'A')

    def test_update_student_grade(self):
        # Add a student to update
        students.append({'id': '002', 'name': 'Jane Doe', 'grade': 'B'})
        
        # Simulate user input
        sys.stdin = StringIO('002\nA+\n')
        
        # Call the update_student_grade function
        update_student_grade()
        
        # Check if the student's grade was updated correctly
        self.assertEqual(students[0]['grade'], 'A+')

    def test_update_student_grade_not_found(self):
        # Simulate user input for non-existent student
        sys.stdin = StringIO('003\nA+\n')
        
        # Capture the output
        output = StringIO()
        sys.stdout = output

        # Call the update_student_grade function
        update_student_grade()
        
        # Check if the correct message was printed
        self.assertIn("Student not found!", output.getvalue())

    def test_display_students(self):
        # Add a student to display
        students.append({'id': '004', 'name': 'Alice', 'grade': 'A'})
        
        # Capture the output
        output = StringIO()
        sys.stdout = output
        
        # Call the display_students function
        display_students()
        
        # Check if the student details are correctly displayed
        self.assertIn("ID: 004, Name: Alice, Grade: A", output.getvalue())

    def test_display_students_empty(self):
        # Capture the output for empty students list
        output = StringIO()
        sys.stdout = output
        
        # Call the display_students function
        display_students()
        
        # Check if the correct message was printed
        self.assertIn("No students to display.", output.getvalue())

    def tearDown(self):
        # Reset stdout and stdin to their original state
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

if __name__ == '__main__':
    unittest.main()

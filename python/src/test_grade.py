
import unittest


from person_def import Person
from course_def import Course
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor
from institution_def import Institution

      

class Test_Grade(unittest.TestCase):
    def test_VerifyGradeSubmission_WhenAllConditionsAreMet_ReturnsTrue_Pytest(self):

        # Arrange
        course = Course("Computer Science", 1234, "Test Class", 3)
        cc = CourseOffering(course, "123", "2023", "1")
        student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
        studentsList = [student1]


        # Act
        cc.submit_grade(student1, 'B')

        # Assert
        # Grades is a dictionary not a list
        # Grades are stored in the dictionary by user name
        # Given this we can test for multiple conditions

        # does 1 and only 1 grade exist?
        assert len(cc.grades) == 1

        # Is the key of the grade the username for student 1?
        assert cc.grades.keys().__contains__("userName")

        #s  Ithe value of this grade a B?
        assert cc.grades.get("userName") == 'B'
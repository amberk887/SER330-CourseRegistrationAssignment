import unittest


from person_def import Person
from course_def import Course
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor
from institution_def import Institution


class Test_Course(unittest.TestCase):
    def test_CourseInit_WhenAllConditionsAreMet_Succeeds(self):
        # Arrange
        course = Course("Engineering", 123, "SER", 3)

        # Act
        course.name = 'Test'
        course.department = "Communications"
        course.credits = 1
        course.number = 456

        # Assert
        assert course.name == 'Test'
        assert course.department == 'Communications'
        assert course.credits == 1
        assert course.number == 456
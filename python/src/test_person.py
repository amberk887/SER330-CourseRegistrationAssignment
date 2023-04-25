
import unittest


from person_def import Person
from course_def import Course
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor
from institution_def import Institution

class TestPerson(unittest.TestCase):
    def test_PersonInit_WhenAllConditionsAreMet_Succeeds(self):
        # Arrange
        person = Person('LastName', 'FirstName', 'School', 'none', 'none', 'none')

        # Act
        person.first_name = 'Amber'
        person.last_name = 'Kusma'
        person.school='Quinnipiac'
        person.date_of_birth = '07/19/2000'
        person.username = 'akusma'
        person.affiliation = 'student'


        # Assert
        assert person.last_name == 'Kusma'
        assert person.first_name == 'Amber'
        assert person.school == 'Quinnipiac'
        assert person.date_of_birth == '07/19/2000'
        assert person.username == 'akusma'
        assert person.affiliation == 'student'

    
if __name__ == '__main__':
    unittest.main() 
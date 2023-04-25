
import unittest


from person_def import Person
from course_def import Course
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor
from institution_def import Institution

class Test_Student(unittest.TestCase):
    def test_StudentInit_WhenAllConditionsAreMet_Succeeds(self):
        ##Arrange
        
        student1 = Student('first','last','school','02/19/2000','flast')
        student2 = Student('Amber','last','school','02/19/2000','flast')
        student3 = Student('emily','last','school','02/19/2000','flast')
        student4 = Student('bob','last','school','02/19/2000','flast')
        
        student_list=[student1,student2,student3,student4]

        course =Course("Computer Science", 1234, "test", 3)
        
        # Need course offerring 
        course1 =  CourseOffering(course, "123", "2021", "3")
        course2 =  CourseOffering(course, "123", "2022", "3")

        student1.last_name='Kusma'
        courseOfferingList=[course1,course2]
        course1.register_students(student_list)

        student1.course_list = courseOfferingList

        #Assert
        assert student1.last_name=='Kusma'
        assert student1.gpa == 0
        assert len(student1.course_list)==2
        assert student1.credits ==6
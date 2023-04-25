
import unittest


from person_def import Person
from course_def import Course
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor
from institution_def import Institution




class Test_Instructor(unittest.TestCase):
    def test_InstructorInit_WhenAllConditionsAreMet_Succeeds(self):
        # Arrange

         # Need instructor
        instructor = Instructor('last','first', 'qu','09/23/1999','username')
        instructor2 = Instructor('last','first', 'qu','09/23/1999','username')
        instructor3 = Instructor('last','first', 'qu','09/23/1999','username')


        # Need course 
        course =Course("Computer Science", 1234, "test", 3)
        
        # Need course offerring 
        co1 =  CourseOffering(course, "123", "2021", "1")
        co2 =  CourseOffering(course, "123", "2022", "3")
        courseOfferingList=[co1,co2]

        co3 = CourseOffering(course,"123","2022","2")
        co4 =  CourseOffering(course,"123","2021","2")
        courseOfferingYear=[co4,co3]

        co5 = CourseOffering(course,"123","2022","2")
        co6 =  CourseOffering(course,"123","2021","1")
        courseOfferingQuarter=[co5,co6]
    
       
        instructor.course_list = courseOfferingList
        instructor2.course_list = courseOfferingYear
        instructor3.course_list=courseOfferingQuarter

        # Act
        returnedCourses = instructor.list_courses()
        returnedCourses2 = instructor.list_courses("2022")
        returnedCourses3=instructor.list_courses("2021","1")

        # Assert
        assert len(returnedCourses3) == 1
        assert len(returnedCourses2) == 1
        assert len(returnedCourses)==len(courseOfferingList)
        
        assert instructor.last_name == 'last'
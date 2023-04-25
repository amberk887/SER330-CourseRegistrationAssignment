
import unittest


from person_def import Person
from course_def import Course
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor
from institution_def import Institution

class Test_Institution(unittest.TestCase):
    def test_VerifyRegisterStudenForCourse_WhenAllConditionsMet(self):

        # Arrange
        # Define a course and a course offering
        #
        department = "ComputerScience"
        courseNumber = 1234
        courseName = "TestClass"
        courseCredits = 3
        courseSectionNumber = 123
        courseOfferYear = "2023"
        courseQuarter = "1"
        course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
        course2 = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
        course3 = Course(department=department, number=courseNumber, name="bio", credits= courseCredits)

        courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)

        # Define a student
        student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")
        student2 = Student("Test", "Test", "School Test", "4/20/2023", "test")

        

        # Define an institution
        institution = Institution("Quinnipiac University", "qu.edu")
        institution2 = Institution("Quinnipiac University", "qu.edu")


        # Create an instructor
        professor = Instructor("last","first",institution,"07/19/2000","username")

        #Add the course to the institution (to the course catalog)
        institution.add_course(course)
        institution.add_course(course2)

        # Add the course to to the planned course offerings
        institution.add_course_offering(courseOffering)

        # Enroll the student into the school
        institution.enroll_student(student1)

        institution.hire_instructor(professor)

        courseSchedule = institution.course_schedule
        # Act
        # Register the student for the course
        institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)

        # Assert

        #testing that only one student is reegistered for a course offering
        assert len(courseOffering.registered_students) == 1
        
        #testing that the course catalog should only be one item long
        assert len(institution.course_catalog)==1

        #testing that the domain is the same as value passeed in
        assert institution.domain=='qu.edu'

        #testing that only one professor exists in the institution
        assert len(institution.faculty_list)==1

        #testing that a course cannot be added twice
        assert institution.add_course(course2) =='Course has already been added'

        #testing that only one student is enrolled in the institution
        assert len(institution.student_list)==1

        #testing that student can only be enrolleed in the institution once
        assert institution.enroll_student(student1)=="Test Test is already enrolled!"

        #testing that professor can only bee hired once
        assert institution.hire_instructor(professor)=='first last already works at this institution!'

        #testing that a student cannot be registered for a class twice
        assert institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)=='\n'+'Test Test is already enrolled in this course'+'\n'

        #testing all possible returns for assign_instructor method
        assert institution.assign_instructor(professor, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)=='\n'+'first last has been assigned to teach course'+'\n'
        assert institution.assign_instructor(professor, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)=='\n'+'first last is already teaching this course'+'\n'
        assert institution.assign_instructor(professor,courseName, department, courseNumber, courseSectionNumber, courseOfferYear, 2)=='Course not found. Please create a course and course offering'
        
        #testing list_course_schedule method with various quarters, years and depts
        assert institution.list_course_schedule("2023","1")!='No offerings during this semester'
        assert institution.list_course_schedule("2023","1",department) !='No offerings during this semester'
        assert institution.list_course_schedule("2022","1") !='No offerings during this semester'
        assert institution.list_course_schedule("2022","1",department) =='No offerings during this semester'

        #testing that an institution with no courses returns that no offerings are scheduled
        assert institution2.list_course_schedule('2022','3')=='No offerings currently scheduled'


        #testing that an unadded course cannot be used to create a course offering
        assert institution.add_course_offering(CourseOffering(course3, courseSectionNumber, courseOfferYear, courseQuarter)) =="Please create a course before creating course offering"


        #testing that TypeErrors will occur when incorrect object type is passed in
        self.assertRaises(TypeError,institution.hire_instructor,course)
        self.assertRaises(TypeError,institution.enroll_student,course)
        self.assertRaises(TypeError,institution.add_course,student1)
        self.assertRaises(TypeError,institution.add_course_offering,student1)





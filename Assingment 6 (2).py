
class Person:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number

    def display_info(self):
        print(f"Name: {self.name}\nContact Number: {self.contact_number}")


class Student:
    def __init__(self, department, semester):
        self.department = department
        self.semester = semester

    def display_info(self):
        print(f"Department: {self.department}\nSemester: {self.semester}")


class Teacher:
    def __init__(self, course, office_number):
        self.course = course
        self.office_number = office_number

    def display_info(self):
        print(f"Course: {self.course}\nOffice Number: {self.office_number}")


class TA(Person, Student, Teacher):
    def __init__(self, name, contact_number, department, semester, course, office_number):
        Person.__init__(self, name, contact_number)
        Student.__init__(self, department, semester)
        Teacher.__init__(self, course, office_number)

    def display_info(self):
        # Call display_info methods of Person, Student, and Teacher
        Person.display_info(self)
        Student.display_info(self)
        Teacher.display_info(self)

# Test the classes
student1 = Student("Computer Science", 3)
teacher1 = Teacher("Computer Networks", 101)
ta1 = TA("Bob", "111-222-3333", "Electrical Engineering", 2, "Introduction to Circuits", 202)

print("Student Information:")
student1.display_info()
print("\nTeacher Information:")
teacher1.display_info()
print("\nTA Information:")
ta1.display_info()

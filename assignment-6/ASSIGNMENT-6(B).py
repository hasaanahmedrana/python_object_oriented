class Person:
    """
    A class representing a generic person.
    Attributes:
    - name (str): The name of the person.
    - contact (str): The contact information of the person.
    Methods:
    - info(): Returns a string with the person's name and contact information.
    """
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    @property
    def name(self):
        return self._name

    @property
    def contact(self):
        return self._contact

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print('Please Enter Name of the appropriate format i.e, string.')

    @contact.setter
    def contact(self, contact):
        if isinstance(contact, str):
            self._contact = contact
        else:
            print('Please Enter Contact of the appropriate format i.e, string.')

    def info(self):
        info = ''
        info += f'Hey my name is {self.name} and my contact number is {self.contact}.\n'
        return info


class Student(Person):
    """
    A class representing a student, inheriting from the Person class.
    Attributes:
    - semester (int): The semester in which the student is enrolled.
    - department (str): The department to which the student belongs.
    Methods:
    - info(): Returns a string with the student's name, contact, semester, and department.
    """
    def __init__(self, name, contact, semester, department):
        Person.__init__(self, name, contact)
        self.semester = semester
        self.department = department

    @property
    def semester(self):
        return self._semester

    @property
    def department(self):
        return self._department

    @semester.setter
    def semester(self, semester):
        if isinstance(semester, int):
            self._semester = semester
        else:
            print('Please Enter Semester of the appropriate format i.e, integer.')

    @department.setter
    def department(self, department):
        if isinstance(department, str):
            self._department = department
        else:
            print('Please Enter Department Name of the appropriate format i.e, string.')

    def info(self):
        info = ''
        info += Person.info(self)
        info += f'I am the Student of {self.semester} Semester at {self.department} department'
        return info


class Teacher(Person):
    """
    A class representing a teacher, inheriting from the Person class.
    Attributes:
    - course (str): The course taught by the teacher.
    - office_number (int): The office number of the teacher.
    Methods:
    - info(): Returns a string with the teacher's name, contact, course, and office number.
    """
    def __init__(self, name, contact, course, office_number):
        Person.__init__(self, name, contact)
        self.course = course
        self.office_number = office_number

    @property
    def course(self):
        return self._course

    @property
    def office_number(self):
        return self._office_number

    @course.setter
    def course(self, course):
        if isinstance(course, str):
            self._course = course
        else:
            print('Please Enter Course Name of the appropriate format i.e, string.')

    @office_number.setter
    def office_number(self, office_number):
        if isinstance(office_number, int):
            self._office_number = office_number
        else:
            print('Please Enter Office Number of the appropriate format i.e, integer.')

    def info(self):
        info = ''
        info += Person.info(self)
        info += f'I am the Teacher Assistant of {self.course}, you can meet me at Room# {self._office_number}'
        return info


class TA(Student, Teacher):
    """
    A class representing a teaching assistant, inheriting from both Student and Teacher classes.
    Attributes:
    (Inherited from Student)
    - semester (int): The semester in which the TA is enrolled.
    - department (str): The department to which the TA belongs.
    (Inherited from Teacher)
    - course (str): The course for which the TA is an assistant.
    - office_number (int): The office number of the TA.
    Methods:
    - info(): Returns a string with the TA's name, contact, semester, department, course, and office number.
    """
    def __init__(self, name, contact, semester, department, course, office_number):
        Student.__init__(self, name, contact, semester, department)
        Teacher.__init__(self, name, contact, course, office_number)

    def info(self):
        info = Student.info(self)
        info += '\n'
        info += Teacher.info(self).split('\n', 1)[1]
        return info


def main():

    print('-------------Testing Student Class:----------------')
    print('Is Student is a person?', issubclass(Student, Person))
    s = Student('Hasaan', '123', 3, 'AI')
    print('Information:')
    print(s.info())
    print()
    print('--------------Testing Teacher Class:-----------------')
    print('Is Teacher is a person?', issubclass(Teacher, Person))
    t = Teacher('Shehryar', '123', 'Artificial Intelligence', 101)
    print('Information:')
    print(t.info())
    print()
    print('-----------Testing Teacher Assistant Class-------------')
    print('Is Teacher Assistant is a Person?', issubclass(TA, Person))
    print('Is Teacher Assistant is a Student?', issubclass(TA, Student))
    print('Is Teacher Assistant is a Teacher?', issubclass(TA, Teacher))
    t = TA('Rayan', '123', 3, 'AI', 'Discrete', 101)
    print('Information:')
    print(t.info())


if __name__ == '__main__':
    main()
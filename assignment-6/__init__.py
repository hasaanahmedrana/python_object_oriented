#-----------------TASK-1------------------------
from math import *
class N_DIMENSIONAL_VECTOR:
    """
    Class representing an N-dimensional vector.
    Attributes:
    - vector: Tuple or list of numeric values representing the components of the vector.
    Methods:
    - __init__(*args): Initializes the vector with the given components.
    - __str__(): Returns a string representation of the vector.
    - magnitude(): Computes and returns the magnitude of the vector.
    - dot_product(other): Computes and returns the dot product with another vector.
    - __add__(other): Adds another vector to the current vector and returns a new vector.
    - __sub__(other): Subtracts another vector from the current vector and returns a new vector.
    - __eq__(other): Checks if two vectors are equal.
    - __ne__(other): Checks if two vectors are not equal.
    - __len__(): Returns the number of components in the vector.
    - is_zero_vector(): Checks if the vector is a zero vector.
    - is_unit_vector(): Checks if the vector is a unit vector.
    """
    def __init__(self, *args):
        self.vector = args

    def __str__(self):
        return f'Vector: {self.vector}'

    def magnitude(self):
        n = 0
        for i in self.vector:
            n += (i**2)
        return round(sqrt(n), 3)

    def dot_product(self, other):
        if len(self.vector) != len(other.vector):
           return 'Dot Product not possible.'
        n = 0
        for i, j in zip(self.vector, other.vector):
            n += (i * j)
        return n

    def __add__(self, other):
        if len(self.vector) != len(other.vector):
            return 'For Addition, dimension of both vectors must be equal'

        lst = []
        for i, j in zip(self.vector, other.vector):
            lst.append(i + j)
        return N_DIMENSIONAL_VECTOR(*lst)

    def __sub__(self, other):
        if len(self.vector) != len(other.vector):
            return 'For Subtraction, dimension of both vectors must be equal'
        lst = []
        for i, j in zip(self.vector, other.vector):
            lst.append(i - j)
        return N_DIMENSIONAL_VECTOR(*lst)

    def __eq__(self, other):
        if len(self.vector) != len(other.vector):
            return False
        for i, j in zip(self.vector, other.vector):
            if i != j:
                return False
        return True

    def __ne__(self, other):
        if len(self.vector) == len(other.vector):
            for i in range(len(self.vector)):
                if self.vector[i] != other.vector[i]:
                    return True
            return False
        else:
            return True

    def __len__(self):
        return len(self.vector)

    def is_zero_vector(self):
        for i in self.vector:
            if i != 0:
                return False
        return True

    def is_unit_vector(self):
        for i in self.vector:
            if i != 1:
                return False
        return True


print('-----------  TASK-2 --------------')
print('----------------------------------')
print()


def main():
    v1 = N_DIMENSIONAL_VECTOR(1, 2, 3, 4)
    v2 = N_DIMENSIONAL_VECTOR(1, 2, 3, 4)
    v3 = N_DIMENSIONAL_VECTOR(5, 6, 7, 8)
    v4 = N_DIMENSIONAL_VECTOR(1, 2, 3, 4, 5, 6, 8)
    v5 = N_DIMENSIONAL_VECTOR(1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    v6 = N_DIMENSIONAL_VECTOR(0, 0, 0, 0, 0, 0, 0, 0)
    v7 = N_DIMENSIONAL_VECTOR(1, 1, 1, 1, 1, 1, 1, 1)

    print('---TESTING STR METHOD---')
    print('V1: ', v1)
    print('V2: ', v2)
    print()
    print('---TESTING MAGNITUDE METHOD---')
    print('Magnitude of V1: ', v1.magnitude())
    print('Magnitude of V3: ', v3.magnitude())
    print('Magnitude of V5: ', v5.magnitude())
    print()
    print('---TESTING DOT PRODUCT METHOD---')
    print('Dot Product of V1 and V2: ', v1.dot_product(v2))
    print('Dot Product of V1 and V3: ', v1.dot_product(v3))
    print('Dot Product of V3 and V4: ', v3.dot_product(v4))
    print()
    print('---TESTING ADDITION METHOD---')
    print('V1 + V2: ', v1 + v2)
    print('V1 + V3: ', v1 + v3)
    print('V3 + V4: ', v3 + v4)
    print()
    print('---TESTING SUBTRACTION METHOD---')
    print('V1 - V2: ', v1 - v2)
    print('V3 - V1: ', v3 - v1)
    print('V4 - V3: ', v4 - v3)
    print()
    print('---TESTING EQUALITY METHOD---')
    print('V1 == V2: ', v1 == v2)
    print('V1 == V3: ', v1 == v3)
    print()
    print('---TESTING INEQUALITY METHOD---')
    print('V1 != V2: ', v1 != v2)
    print('V1 != V3: ', v1 != v3)
    print()
    print('---TESTING LENGTH METHOD---')
    print('Length of V1: ', len(v1))
    print('Length of V5: ', len(v5))
    print()
    print('---TESTING IS_ZERO_VECTOR METHOD---')
    print('Is V1 a zero vector? ', v1.is_zero_vector())
    print('Is V6 a zero vector? ', v6.is_zero_vector())
    print()
    print('---TESTING IS_UNIT_VECTOR METHOD---')
    print('Is V1 a unit vector? ', v1.is_unit_vector())
    print('Is V7 a unit vector? ', v7.is_unit_vector())



if __name__ == '__main__':
    main()

print()
print('-----------  TASK-2 --------------')
print('----------------------------------')
print()

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

print('-------------TASK 3-----------')
print('-----------ON THE SCREEN-----------')

from abc import *
from tkinter import *
from math import pi, sqrt


class SHAPES(ABC):
    """ ABSTRACT CLASS SHAPES"""
    @abstractmethod
    def __init__(self, x, y, color):
        """
        ABSRACT METHOD
        Initialize the shape with its position and color.
        Parameters:
        - x (int): x-coordinate of the shape.
        - y (int): y-coordinate of the shape.
        - color (str): Color of the shape.
        """
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def give_area(self):
        pass

    @abstractmethod
    def give_perimeter(self):
        pass

    @abstractmethod
    def drawing_on_canvas(self, c):
        pass


class RECTANGLE(SHAPES):
    def __init__(self, x, y, color, height, width):
        SHAPES.__init__(self, x, y, color)
        self.height = height
        self.width = width

    def give_area(self):
        return self.height * self.width

    def give_perimeter(self):
        return 2 * (self.height + self.width)

    def drawing_on_canvas(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
        canvas.create_text(self.x+55, self.y+35, text='Rectangle', font=('Arial', 10, 'bold'), fill='white')


class SQUARE(RECTANGLE):
    def __init__(self, x, y, color, side):
        RECTANGLE.__init__(self, x, y, color, side, side)
        self.side = side

    def give_area(self):
        return self.side**2

    def give_perimeter(self):
        return 4 * self.side

    def drawing_on_canvas(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.side, self.y + self.side, fill=self.color)
        canvas.create_text(self.x+40, self.y+35, text='Square', font=('Arial', 10, 'bold'), fill='black')


class CIRCLE(SHAPES):
    def __init__(self, x, y, color, radius):
        SHAPES.__init__(self, x, y, color)
        self.radius = radius

    def give_area(self):
        return pi * self.radius**2

    def give_perimeter(self):
        return 2 * pi * self.radius

    def drawing_on_canvas(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill = self.color)
        canvas.create_text(self.x, self.y, text='Circle', font=('Arial', 10, 'bold'), fill='white')


class OVAL(CIRCLE):
    def __init__(self, x, y, color, radius, radius2):
        CIRCLE.__init__(self, x, y, color, radius)
        self.radius2 = radius2

    def give_area(self):
        return pi * self.radius * self.radius2

    def give_perimeter(self):
        a = self.radius
        b = self.radius2
        return pi * (3*(a + b) - sqrt((3*a + b) * (a + 3*b)))

    def drawing_on_canvas(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius2, self.x + self.radius, self.y + self.radius2, fill=self.color)
        canvas.create_text(self.x, self.y, text='Oval', font=('Arial', 10, 'bold'), fill='white')


rectangle = RECTANGLE(30, 50, 'red', 70, 120)
circle = CIRCLE(210, 170, 'blue', 50)
square = SQUARE(250, 250, 'yellow', 80)
oval = OVAL(450, 350, 'purple', 50, 100)

root = Tk()
root.title(" -: DIFFERENT SHAPES :- ")
root.geometry("600x500")
canvas = Canvas(root, width=600, height=500, bg='black')
canvas.pack()
rectangle.drawing_on_canvas(canvas)
circle.drawing_on_canvas(canvas)
square.drawing_on_canvas(canvas)
oval.drawing_on_canvas(canvas)
root.mainloop()

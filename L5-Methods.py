'''
METHODS (are the functions which associate with the object(or objects) in a class.)
(they determine the behaviour of the objects and how they interact with their state.)
  
There are three type of methods:
1-Instance: deal with instance(objects)attributes.
2-Class: deak with class attributes.
3-Static: When method has nothing to do with instance or Class.
'''
class Student:
    School = 'Educators'
    campus = 'City'
    
    def __init__(self, roll_no, marks):
        self.roll_no = roll_no
        self.__marks = marks
        
    @property                             #INSTANCE METHOD
    def marks(self):  
        return self.__marks
    
    @marks.setter
    def marks(self, new):
        if isinstance(new,(int or float)):
            self.__marks = new
    
    @classmethod                            # CLASS METHOD
    def school(cls):
        return f'{cls.School} , {cls.campus}'
    
    @staticmethod                            # STATIC METHOD
    def info():
        return 'This is a student class...Each student have a unique roll number. These are the students of the The educators.'
    
s1 = Student(7,97)
print(s1.marks)
print(Student.school())
print(Student.info())
    
    
    
# Instance methods:
class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def find_diameter(self):
        return self.radius*2


my_circle = Circle(2)
print(my_circle.radius)
a = (my_circle.find_diameter())
print(a)


# example:
class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Please Enter Valid Item list.')

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('Enter a valid item.')

    def add_multiple_items(self, items):
        for each in items:
            self.add_item(each)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)

    def check_item(self, item):
        return item in self._items

    def display_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)


my_bag = Backpack()


print(my_bag.items)
my_bag.items = ['water-bottles', 'notebook', 'books', 'stationery']
my_bag.add_item('pen')
print(my_bag.items)
my_bag.remove_item('books')
print(my_bag.items)
my_bag.remove_item('books')
print(my_bag.items)
print(my_bag.check_item('pen'))
my_bag.add_multiple_items(['pencil', 'personal diary', 'keys'])
print(my_bag.items)

print(f' UNSORTED ITEM LIST: {my_bag.display_items()}')
print(f' SORTED ITEM LIST: {my_bag.display_items(True)}')
print()
# Default Arguments:
# rule 1: they should be on most right place.
# rule 2: putting no space around equal sign between argument and value.


class Game:


    def __init__(self, x, y):
        self.x = x
        self.y = y

     # def move_up(self, change = 5):     #wrong way
    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=2):
        self.x += change

    def move_left(self, change=2):
        self.x -= change


print('-------default argument---------')
player = Game(5, 5)
print(f'Player original position is :{player.x},{player.y}')
player.move_up()
print(f'Player moved up position by default: {player.x},{player.y}')
player.move_right(20)
print(f'Player moved right by 20 value given: {player.x},{player.y}')


# METHODS MINI PROJECT:
class Class:
    student = {}
    id = 1


    def __init__(self, name, age, courses):

        self._name = name
        self._age = age
        self._courses = courses
        self.id = Class.id
        Class.id += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print('Enter Valid Name.')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            print('Enter Valid Age.')

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, new_courses):
        if isinstance(new_courses, list):
            self._courses = new_courses
        else:
            print('Enter Valid Course list.')

    def adding(self):
        Class.student[self.id] = [self.name, self.age, self.courses]

    @staticmethod
    def display_students():
        for i, j in Class.student.items():
            print(f'{i} {j[0]} {j[1]},{j[2]}')


s1 = Class('ROSS', 34, ['PF', 'ICT'])
s2 = Class('PHOEBE', 37, ['HISTORY', 'STATS'])
s3 = Class('MONICA', 31, ['GEOLOGY, HOME ECONOMICS'])
s1.adding()
s2.adding()
s3.adding()
Class.display_students()

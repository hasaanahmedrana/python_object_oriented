"""INHERITANCE : (creating classes which inherit attributes and methods from other classes.)

 --> prevent overwriting, reuse of code,  better readability with more clean code. """
class Polygon:
    def __init__(self, num_sides, color):
        self.sides = num_sides
        self.color = color


class Triangle(Polygon):
    SIDES = 3

    def __init__(self, height, base, color):
        Polygon.__init__(self, Triangle.SIDES, color)
        self.height = height
        self.base = base


my_tri = Triangle(3, 4, 'blue')
print(my_tri.sides)


class Employee:
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary


class Programmers(Employee):
    def __init__(self, full_name, salary, programming_language):
        Employee.__init__(self, full_name, salary)
        self.programming_language = programming_language


employee1 = Programmers('ZOE', 200000, 'Python')
print(employee1.full_name)
print(employee1.salary)
print(employee1.programming_language)


class Character:
    def __init__(self, x, y, number_of_lives):
        self.x = x
        self.y = y
        self.number_of_lives = number_of_lives


class Player(Character):
    INITIAL_X = INITIAL_Y = 0
    LIVES = 10

    def __init__(self, score):
        Character.__init__(self, Player.INITIAL_X, Player.INITIAL_Y, Player.LIVES)
        self.score = score


class Enemy(Character):

    def __init__(self, x=15, y=15, lives=10, is_poisonous=False):
        Character.__init__(self, x, y, lives)
        self.is_poisonous = is_poisonous


player = Player(score=5)
print(player.x)
print(player.y)
print(player.number_of_lives)
print(player.score)
print('-----------------')
enemy = Enemy(is_poisonous=True)
print(enemy.x)
print(enemy.y)
print(enemy.is_poisonous)
print(enemy.number_of_lives)
print('++++++++++++++++++++++++++++++++')


class Polygon:
    def __init__(self, num_sides, color):
        self.sides = num_sides
        self.color = color

    def describe_polygon(self):
        return f"This polygon has {self.sides} sides and it's {self.color}."


class Triangle(Polygon):

    SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.SIDES, color)
        self.base = base
        self.height = height

    def find_area(self):
        return (self.base * self.height)/2


class Square(Polygon):

    SIDES = 5
    def __init__(self, side_length, color):
        Polygon.__init__(self, Square.SIDES, color)
        self.sides_length = side_length

    def find_area(self):
        return self.sides_length*4


triangle = Triangle(3, 2, 'black')
print(triangle.describe_polygon())
print(triangle.find_area())
print('------------------------------------')
square = Square(4, 'red')
print(square.describe_polygon())
print(square.find_area())


# OVERRIDING:
print('----------------OVER-RIDING------------------')


class Teacher:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def introduction(self):
        print(f'Hey ! I am your teacher and my name is {self.name}')


class ArtsTeacher(Teacher):
    # pass
    def introduction(self):
        print('Welcome to art class!')
        #print(f'Hey ! I am your teacher and my name is {self.name}')
        super().introduction()


x = ArtsTeacher('Zoe', 23456)
x.introduction()

print('-----------------------------')
# EXAMPLE:
class Backpack:
    def __init__(self):
        self.items = []

    def add_snacks(self, snack):
        print('Time to add snack in you bag..')
        self.items.append(snack)
        print(f'{snack.capitalize()} has been added in the bag')


class SchoolBackpack(Backpack):
    def add_snacks(self, snack):
        print('You are going to school. So')
        Backpack.add_snacks(self, snack)
        print('I love it.')


y = Backpack()
y.add_snacks('candy')

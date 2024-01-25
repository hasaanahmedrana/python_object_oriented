"""PROPERTY: (A better alternative of getter and setter which is more practical)."""

# Simple Code(in which no input validation was required).
class Dog:
    def __init__(self, age):
        self.age = age


dog1 = Dog(4)
print(f'My dog is {dog1.age} year old')
dog1.age += 1
print()
print(f'My dog is now {dog1.age} year old')

# Code with Getter and setter (When validation was required, we made attribute private and create getter and setter).


class Dog:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and 30 > age > 0:          # it is validating input.
            self._age = age
        else:
            print('Enter valid name.')


# print(dog2.name)    # can't access this way.
dog2 = Dog(4)
print(f'My dog is {dog2.get_age()} year old')   # to access the name we need to caller getter everytime,
print()                                               # so this approach, not so practical
dog2.set_age(dog2.get_age() + 1)
print(f'My dog is now {dog2.get_age()} year old')


#  CODE 3 (using getter ,setter and property(it doesn't need to change name of attribute everywhere).
class Dog:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and 30 > age > 0:          # it is validating input.
            self._age = age
        else:
            print('Enter valid name.')

    age = property(get_age, set_age)


dog2 = Dog(4)
print(f'My dog is {dog2.age} year old')   # to access the name we need to caller getter everytime,
print()                                    # so this approach, not so practical
dog2.age += 1
print(f'My dog is now {dog2.age} year old')


# EXAMPLE 2:
class Circle:
    valid_colors = ['red', 'blue', 'green']

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color
        
    def get_radius(self):
        return self._radius

    def set_radius(self, new_radii):
        if isinstance(new_radii, int or float) and new_radii > 0:
            self._radius = new_radii
        else:
            print('Enter Valid Radius.')

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.valid_colors:
            self._color = new_color
        else:
            print('Enter Valid Color.')
    color = property(get_color, set_color)


circle = Circle(3, 'red')

print(circle.color)
circle.color = 'pink'
print(circle.color)
circle.color = 'green'
print(circle.color)



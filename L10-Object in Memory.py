"""Python is an object-oriented programming language. Everything in python is an object.You can see this below."""
print(object)
print(isinstance(2, object))
print(isinstance(2.7, object))
print(isinstance('HEY', object))
print(isinstance([1, 2, 3], object))
print(isinstance({1, 2, 3}, object))
print(isinstance((1, 2, 3), object))
print(isinstance({1: 'okay', 2: 'not okay'}, object))
print(isinstance(False, object))


def function():
    return "HEY I'M A FUNCTION "


print(isinstance(function(), object))

# EVERY OBJECT STORE IN MEMORY WITH A UNIQUE ID(LOCATION).
# ID() FUNCTION can be used to know the exact address of the object in the memory.
#   " Every object have a unique ID during its lifetime.
#     When object is deleted, and a new object created the new one can have that exact same id
#     because no existing object have that id at that time. "

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(f'ID of x: {id(x)} , ID of y: {id(y)}')


class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items


my_backpack = Backpack()
your_backpack = Backpack()
print(f'ID of my bag: {id(my_backpack)} , ID of your bag: {id(your_backpack)}')

# 'is'  ans 'is not' Operator :
# This operators tell about whether to name actually refer to same object or not.
# It is different from ==, is deal with id while == with values.

x = [1, 2]
y = [1, 2]
print('Example 1:')
print(x is y)
print(x is not y)
print(x == y)

print('Example 2:')
x = y = [1, 2]
print(x is y)
print(x is not y)
print(x == y)

# UNEXPECTED 'is' OPERATOR RESULTS:
# In python there's a specific range of integers as array stored in memory as an object already.
# so even when we create two objects with same value in range(-5 to 256 in IDLE, different in all environments).
# It refers to same object and is operator show output of True
a = 4
b = 4
print(a is b)
# String interning
x = 'HEY'
y = 'HEY'
z = 'HEY'

print(x is y is z)
print(f'ID of x: {id(x)} , ID of y: {id(y)}, ID of x {id(z)}')


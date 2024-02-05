"""   Aliasing:

     In Python, it is the same thing, using two or more references to the same object in memory.
     Simply having multiple names of a single object and any of that names can be used to access the object.
     We can check that all names refer to the same object using “id() function”, they all will have the same id."""


a = [3, 6, 9]
b = a
b[2] = 77
print(a)

"""
Mutable Objects: (modifications can be made):
--->"Highly memory efficient, Real World Objects,higher risk of bugs"
Immutable Objects: (Can't be modified):
--->"Low bugs risk, Less memory efficient,easy to understand with no hidden meanings"""


# **Intention just to take any list and return sum of its all absolute value without affecting real list.**
def sum_of_absolute(x):
    for i in range(len(x)):
        x[i] = abs(x[i])
    return sum(x)


z = [-2, -3, -7]
print('Z before function:', z)
sum_of_absolute(z)
print('Z after function:', z)


# ** we didn't want any modification in real list.**
def remove_elements_with_even_value(dictionary):
    for key, value in (dictionary.items()):
        if value % 2 == 0:
            del dictionary[key]
    print(dictionary)


my_dict = {'A': 3, "B": 4 , "C": 5}
remove_elements_with_even_value(my_dict)
"""   Expected results is dictionary as {'A': 3, 'C': 5}
but it will give error as the length of the dictionary keep changing during iteration.
This issue can be resolved by using CLONING"""

# CLONING : creating exact copy of the object.


def remove_elements_with_even_value(dictionary):
    for key, value in (dictionary.copy().items()):
        if value % 2 == 0:
            del dictionary[key]
    print(dictionary)


my_dict = {'A': 3, "B": 4, "C": 5}
remove_elements_with_even_value(my_dict)

"""
METHODS: (these are the specific functions associated with specific class or object)
GETTERS: (methods or functions which are used to get the value of attribute,
         they prevent misuse of attributes(unofficial changes) and control data)
"""

class Classroom:
    def __init__(self, name, id, gpa):
        self.name = name
        self.__id = id
        self.__gpa = gpa

    def get_id(self):               # convention of naming getter --> "get_<attribute>"
        return self.__id

    def get_gpa(self):
        return self.__gpa


student = Classroom("ALI", 27, 3.7)


# print(student.gpa)               # can't access it as it does not exist.
print(student.get_gpa())           # way o accessing getter.

# SETTERS(they are used to set the value of the instance attributes).
# (help to validate the new value before assigning it to the attribute in modification).
# Example:


class Dog:
    def __init__(self, name, breed):

        self._name = name                # let the  name of the dog is non-public data.
        self.breed = breed

    def get_name(self):                  # using getter to get/use the name of dog in the code.
        return self._name

    def set_name(self, new_name):        # use to set/modify the name of the dog
        if isinstance(new_name, str) and new_name.isalpha():   # these condition make sure the name is of class
            self._name = new_name                              # string and only contain alphabets
        else:
            print(' Please enter appropriate new name')         # if the required condition not fulfil,
            print()                                              # we can handle it in our own way

dog1 = Dog("tom", "hh")


print("My pet name is :", dog1.get_name())
# print(dog1.name)
dog1.set_name("jerry")           # it modifies name of dog to jerry
# dog1.set_name('123')           #these func will not make any changes as they don't fulfil conditions.
# dog1.set_name('alien22')
print("My pet name is :", dog1.get_name())

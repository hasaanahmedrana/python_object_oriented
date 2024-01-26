# NAME CONVENTION FOR PRIVATE DATA
class Car:
    def __init__(self, model, year):
        self.model = model            # public attribute
        self._year = year             # private attribute as convention of naming private attribute (_<name>) used


car1 = Car("audi", 2012)
car2 = Car("mehran", 2018)

print(car1.model)            # public attributes can be access directly
print(car2.model)

print(car1._year)            # private attributes can't bes directly access as public attributes
print(car2._year)
# print(car1.year)           # can't be access this way as they don't exist
# print(car2.year)


# MANGLING OF NAME FOR PRIVATE DATA
class Classroom:
    def __init__(self, id, gpa, name):
        self.name = name                    # public attribute
        self._id = id                       # private (by name convention)
        self.__gpa = gpa                    # private (by mangling of name)


student = Classroom(27, 3.93, "jack")
print(student.name)
print(student._id)
# print(student.gpa)           # doesn't exist
# print(student.__gpa)         # doesn't exist
print(student._Classroom__gpa)
# ---------------IMPORTANT--------------------
# after mangling the name of <attribute> convert into "< _class name __attribute>"
# we can access it in this way ,but we should not , not a good way

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
    - __mul__(other): Multiplies scalar with the current vector and returns a new vector.
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

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            lst = []
            for i in self.vector:
                lst.append(i * other)
            return N_DIMENSIONAL_VECTOR(*lst)
        else:
            return 'Multiplication not possible.'

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
    print()
    print('---TESTING MULTIPLICATION METHOD---')
    print('V1 * 2: ', v1 * 2)
    print('V2 * 2.5: ', v2 * 2.5)



if __name__ == '__main__':
    main()
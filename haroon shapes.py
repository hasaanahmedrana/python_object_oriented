from math import pi, sqrt

class Canvas:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f'Canvas Dimensions: {self.height} by {self.width}\n'

class Outline:
    def __init__(self):
        self.outline_width = 2
        self.outline_color = "Black"

class Shape:
    def __init__(self, name, background):
        self.name = name
        self.background = background

    def perimeter(self):
        pass

    def area(self):
        pass

class Square(Shape, Outline):
    def __init__(self, name, background, length):
        super().__init__(name, background)
        Outline.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

    def __str__(self):
        return f'Shape: {self.name}, Length: {self.length}, Outline Width & Color: {self.outline_width} / {self.outline_color}\nBackground: {self.background}, Area: {self.area()}, Perimeter: {self.perimeter()}\n'


class Rectangle(Shape, Outline):
    def __init__(self, name, background, length, width):
        super().__init__(name, background)
        Outline.__init__(self)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __str__(self):
        return f'Shape: {self.name}, Length: {self.length}, Width: {self.width}\nOutline Width & Color: {self.outline_width} / {self.outline_color}\nBackground: {self.background}, Area: {self.area()}, Perimeter: {self.perimeter()}\n'

class Circle(Shape, Outline):
    def __init__(self, name, background, radius):
        super().__init__(name, background)
        Outline.__init__(self)
        self.radius = radius

    def area(self):
        return self.radius ** 2 * pi

    def circumference(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f'Shape: {self.name}, Radius: {self.radius}\nOutline Width & Color: {self.outline_width} / {self.outline_color}\nArea: {self.area()}, Circumference: {self.circumference()}\n'

class Oval(Shape, Outline):
    def __init__(self, name, background, radius1, radius2):
        super().__init__(name, background)
        Outline.__init__(self)
        self.radius1 = radius1
        self.radius2 = radius2

    def area(self):
        return pi * self.radius1 * self.radius2

    def circumference(self):
        return 2 * pi * sqrt((self.radius1 ** 2 + self.radius2 ** 2) / 2)

    def __str__(self):
        return f'Shape: {self.name}, Radius1: {self.radius1}, Radius2: {self.radius2}\nOutline Width & Color: {self.outline_width} / {self.outline_color}\nArea: {round(self.area(), 2)}, Circumference: {round(self.circumference(), 2)}\n'

class Triangle(Shape, Outline):
    def __init__(self, name, background, height, base):
        super().__init__(name, background)
        Outline.__init__(self)
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self, a, b, c):
        print(f'Perimeter: {a + b + c}')

    def __str__(self):
        return f'Shape: {self.name}, Height: {self.height}, Base: {self.base}\nOutline Width & Color: {self.outline_width} / {self.outline_color}\nArea: {self.area()}'

def main():
    canvas = Canvas(30, 40)
    print(canvas)

    square = Square("Square", "Blue", 5)
    print(square)

    rectangle = Rectangle("Rectangle", "Blue", 5, 10)
    print(rectangle)

    circle = Circle("Circle", "Red", 7)
    print(circle)

    oval = Oval("Oval", "Orange", 7, 9)
    print(oval)

    triangle = Triangle("Triangle", "Yellow", 3, 5)
    print(triangle)
    triangle.perimeter(1, 2, 3)

if __name__ == '__main__':
    main()

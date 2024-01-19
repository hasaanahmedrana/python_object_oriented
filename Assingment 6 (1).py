

import abc
import tkinter as tk

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Oval(Circle):
    def __init__(self, major_axis, minor_axis):
        super().__init__(max(major_axis, minor_axis))
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def area(self):
        return 3.14 * self.major_axis * self.minor_axis

shapes = [Rectangle(5, 10), Circle(7), Square(4), Oval(8, 5)]

for shape in shapes:
    print(f"Area of the {type(shape)}: {shape.area()}")

root = tk.Tk()
root.title("Shapes Drawing")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

rectangle = Rectangle(50, 100)
canvas.create_rectangle(10, 10, 10 + rectangle.width, 10 + rectangle.height, fill="blue")

square = Square(50)
canvas.create_rectangle(150, 10, 150 + square.width, 10 + square.height, fill="red")

circle = Circle(30)
canvas.create_oval(10, 150, 10 + 2 * circle.radius, 150 + 2 * circle.radius, fill="green")

oval = Oval(60, 40)
canvas.create_oval(150, 150, 150 + oval.major_axis * 2, 150 + oval.minor_axis * 2, fill="orange")

root.mainloop()

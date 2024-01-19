


from abc import *
from tkinter import *
from math import pi, sqrt


class Shapes(ABC):

    @abstractmethod
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self, canvas):
        pass


class Rectangle(Shapes):
    def __init__(self, x, y, color, height, width):
        Shapes.__init__(self, x, y, color)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)


class Circle(Shapes):
    def __init__(self, x, y, color, radius):
        Shapes.__init__(self, x, y, color)
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def give_perimeter(self):
        return 2 * pi * self.radius

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius,
                            fill=self.color)


class Square(Rectangle):
    def __init__(self, x, y, color, side):
        Rectangle.__init__(self, x, y, color, side, side)
        self.side = side

    def area(self):
        return self.side**2

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.side, self.y + self.side, fill=self.color)


class Oval(Circle):
    def __init__(self, x, y, color, radius, radius2):
        Circle.__init__(self, x, y, color, radius)
        self.radius2 = radius2

    def area(self):
        return pi * self.radius * self.radius2

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius2, self.x + self.radius,
                            self.y + self.radius2, fill=self.color)


rectangle = Rectangle(150, 50, 'white', 70, 120)
circle = Circle(100, 190, 'purple', 50)
square = Square(350, 200, 'green', 100)
oval = Oval(220, 350, 'orange', 100, 50)

root = Tk()
root.title("Shapes")
root.geometry("700x700")
canvas = Canvas(root, width=600, height=500, bg='pink')
canvas.pack()
rectangle.draw(canvas)
circle.draw(canvas)
square.draw(canvas)
oval.draw(canvas)
root.mainloop()

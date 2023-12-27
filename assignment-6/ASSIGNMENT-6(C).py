#-------------TASK 3-----------

from abc import *
from tkinter import *
from math import pi, sqrt


class SHAPES(ABC):
    """ ABSTRACT CLASS SHAPES"""
    @abstractmethod
    def __init__(self, x, y, color):
        """
        ABSRACT METHOD
        Initialize the shape with its position and color.
        Parameters:
        - x (int): x-coordinate of the shape.
        - y (int): y-coordinate of the shape.
        - color (str): Color of the shape.
        """
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def give_area(self):
        pass

    @abstractmethod
    def give_perimeter(self):
        pass

    @abstractmethod
    def drawing_on_canvas(self, c):
        pass


class RECTANGLE(SHAPES):
    def __init__(self, x, y, color, height, width):
        SHAPES.__init__(self, x, y, color)
        self.height = height
        self.width = width

    def give_area(self):
        return self.height * self.width

    def give_perimeter(self):
        return 2 * (self.height + self.width)

    def drawing_on_canvas(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
        canvas.create_text(self.x+55, self.y+35, text='Rectangle', font=('Arial', 10, 'bold'), fill='white')


class SQUARE(RECTANGLE):
    def __init__(self, x, y, color, side):
        RECTANGLE.__init__(self, x, y, color, side, side)
        self.side = side

    def give_area(self):
        return self.side**2

    def give_perimeter(self):
        return 4 * self.side

    def drawing_on_canvas(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.side, self.y + self.side, fill=self.color)
        canvas.create_text(self.x+40, self.y+35, text='Square', font=('Arial', 10, 'bold'), fill='black')


class CIRCLE(SHAPES):
    def __init__(self, x, y, color, radius):
        SHAPES.__init__(self, x, y, color)
        self.radius = radius

    def give_area(self):
        return pi * self.radius**2

    def give_perimeter(self):
        return 2 * pi * self.radius

    def drawing_on_canvas(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill = self.color)
        canvas.create_text(self.x, self.y, text='Circle', font=('Arial', 10, 'bold'), fill='white')


class OVAL(CIRCLE):
    def __init__(self, x, y, color, radius, radius2):
        CIRCLE.__init__(self, x, y, color, radius)
        self.radius2 = radius2

    def give_area(self):
        return pi * self.radius * self.radius2

    def give_perimeter(self):
        a = self.radius
        b = self.radius2
        return pi * (3*(a + b) - sqrt((3*a + b) * (a + 3*b)))

    def drawing_on_canvas(self,canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius2, self.x + self.radius, self.y + self.radius2, fill=self.color)
        canvas.create_text(self.x, self.y, text='Oval', font=('Arial', 10, 'bold'), fill='white')


rectangle = RECTANGLE(30, 50, 'red', 70, 120)
circle = CIRCLE(210, 170, 'blue', 50)
square = SQUARE(250, 250, 'yellow', 80)
oval = OVAL(450, 350, 'purple', 50, 100)

root = Tk()
root.title(" -: DIFFERENT SHAPES :- ")
root.geometry("600x500")
canvas = Canvas(root, width=600, height=500, bg='black')
canvas.pack()
rectangle.drawing_on_canvas(canvas)
circle.drawing_on_canvas(canvas)
square.drawing_on_canvas(canvas)
oval.drawing_on_canvas(canvas)
root.mainloop()

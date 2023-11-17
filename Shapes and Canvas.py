from abc import (ABC,abstractmethod)
import math

class Canvas:

    def __init__(self,width, length):
        self.width = width
        self.length = length
        self.shapes = []

    def __str__(self):
        return f"!-----CREATING CANVAS-----!\nCanvas Size: {self.width}  By  {self.length}\n"

    def add_shape(self,shape):
        self.shapes.append(shape)

    def print_shape(self):
        for shape in self.shapes:
            print(shape)
            print("-------------------------------------------------------------------------")

class Outline:

    def __init__(self,o_width,o_color):
        self.outline_width = o_width
        self.outline_color = o_color

    def __str__(self):
        return f"Outline Width: {self.outline_width}mm   Outline Color: {self.outline_color}"
    
class Shape(Outline,ABC):

    def __init__(self,name,color,o_width,o_color):
        super().__init__(o_width,o_color)
        self.name = name
        self.color =color

    def __str__(self):
        return f"Shape Name: {self.name}   Shape Color: {self.color}   {super().__str__()}"
    
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square (Shape):

    def __init__(self, name, color, len, o_width, o_color):
        super().__init__(name, color, o_width, o_color)
        self.length = len
        self.width = len

    def __str__(self):
        return f"{super().__str__()}   Length: {self.length}cm   Width: {self.width}cm\nArea: {self.area()}   Perimeter: {self.perimeter()}"
    
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)

class Rectangle(Square):

    def __init__(self, name, color, len, wid, o_width, o_color):
        super().__init__(name, color, len, o_width, o_color)
        self.width = wid

    def __str__(self):
        return super().__str__()
    
    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()

class Circle(Shape):

    def __init__(self, name, color,r, o_width, o_color):
        super().__init__(name, color, o_width, o_color)
        self.radius = r

    def __str__(self):
        return f"{super().__str__()}   Radius: {self.radius}cm\nArea: {self.area():0.4f}   Circumference: {self.perimeter():0.4f}"
    
    def area(self):
        return (math.pi * (self.radius**2))
    
    def perimeter(self): #Circumference
        return (2*math.pi*self.radius)

class Triangle(Shape):

    def __init__(self, name, color,base, height, o_width, o_color):
        super().__init__(name, color, o_width, o_color)
        self.base = base
        self.height = height
        self.hyp = (self.base**2+self.height**2)**0.5

    def __str__(self):
        return f"{super().__str__()}   Base: {self.base}cm   Height: {self.height}cm   Hypotenuse: {self.hyp:0.2f}\nArea: {int(self.area())}   Perimeter: {self.perimeter():0.4f}"

    def area(self):
        return 0.5*self.base*self.height
    
    def perimeter(self):
        return self.base+self.height+self.hyp

def main():

    c = Canvas(30,20)
    print(c)
    s = Square("Square","Red",5,2,"Black")
    c.add_shape(s)
    r = Rectangle("Rectangle","Blue",2,4,3,"White")
    c.add_shape(r)
    cir = Circle("Circle","Yellow",3,3,"Brown")
    c.add_shape(cir)
    t = Triangle("Triangle","Orange",2,4,4,"Green")
    c.add_shape(t)

    c.print_shape()

main()

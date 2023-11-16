from Author import Author
class Book:
    """
        Represents a book with a name, author, price, and quantity in stock.
        Attributes:
            name: The name of the book.
            author: An instance of the Author class representing the book's author.
            price: The price of the book(+ve)
            qty_in_stock: The quantity of the book in stock (0 or +ve).

        Methods:
            __init__(n: Initializes a new Book instance.
            getAuthorName(): Returns the name of the author of this book.
            print(): Returns a  string representation of the book.
            And all the getter setters of each attribute.
        Properties:
             book: returns the complete info of the Book.
        """
    def __init__(self, name, author, price, qty_in_stock):
        self.set_name(name)
        self.set_author(author)
        self.set_price(price)
        self.set_qty_in_stock(qty_in_stock)

    def get_name(self):
        return self.__name

    def set_name(self, to_set):
        if isinstance(to_set, str):
            self.__name = to_set
        else:
            raise ValueError('Name is not of appropriate format.')

    def get_price(self):
        return self.__price

    def set_price(self, to_set):
        if isinstance(to_set, int) and to_set >= 1:
            self.__price = to_set
        else:
            raise ValueError("Price must be a positive integer.")

    def get_author(self):
        return self.__author

    def set_author(self, author):
        if isinstance(author, Author):
            self.__author = author
        else:
            raise ValueError('Author must be an instance of the Author class')

    def get_qty_in_stock(self):
        return self.__qty_in_stock

    def set_qty_in_stock(self, to_set):
        if isinstance(to_set, int) and to_set >= 0:
            self.__qty_in_stock = to_set
        else:
            raise ValueError("Quantity is not of required format or can't be less than zero.")
    
    def print(self):
        return f"'{self.get_name()}' by {self.get_author()} "

    def getAuthorName(self):
        x = self.get_author()
        return x.name
    @property
    def book(self):
        x=  f'Book: {self.get_name()}\n Author: {self.get_author().name}'
        y=  f' Price: {self.get_price()}\n Quantity in Stock: {self.get_qty_in_stock()}'
        return f'{x}\n{y}'



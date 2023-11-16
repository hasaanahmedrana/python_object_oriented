# ------------CLASS AUTHOR----------

class Author:
    """
       Represents an author with a name, gender, and email.
       Attributes:
           name : The name of the author.
           gender : The gender of the author.
           email : The email address of the author.
           All attributes are string.
       Methods:
           __init__()Initializes a new Author instance.
           __str__(): Returns  string representation of the author.
        Properties:
            Getter and setter of each attribute.
       """
    def __init__(self, name, gender, email):
        self.name = name
        self.gender = gender
        self.email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, to_set):
        if isinstance(to_set, str):
            self.__name = to_set
        else:
            raise ValueError('Name is not of appropriate format.')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, to_set):
        genders = ('M', 'F', 'O')  # M-male, F-female, O-others
        if to_set.isalpha() and to_set in genders:
            self.__gender = to_set
        else:
            raise ValueError('Gender is not of appropriate format.')

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, to_set):
        if isinstance(to_set, str):
            self.__email = to_set
        else:
            print('Email is not of appropriate format.')

    def __str__(self):
        return f"{self.name} ({self.gender})  @{self.email}"


# -----------------CLASS BOOK-----------------
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

    def getAuthorName(self):
        x = self.get_author()
        return x.name

    @property
    def book(self):
        return f'Book: {self.get_name()}\n Author: {self.get_author().name}\n Price: {self.get_price()}\n Quantity in Stock: {self.get_qty_in_stock()}'


def main():
    Jay_Asher = Author('Jay Asher', 'M', 'jay123@gmail.com')
    book_1 = Book('13 Reasons Why!', Jay_Asher, 1200, 17)
    print('Author name of the book:', book_1.getAuthorName())
    print()
    print("Author's Detail: ", book_1.get_author())
    print()
    print(" Complete Book's Detail:\n", book_1.book)
main()

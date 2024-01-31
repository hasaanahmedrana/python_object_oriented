""" SPECIAL METHODS """
# STR method.

a = 123
print(str(a))
print(a.__str__())

class Student:


    def __init__(self, name, fathers_name, roll_number):
        self.name = name
        self.fathers_name = fathers_name
        self.roll_number = roll_number

    def __str__(self):
        return f'name: {self.name} |'\
               f'father name:  {self.fathers_name} |'\
               f'roll number: {self.roll_number} '


x = Student('Ash', 'Riz', 523)
print(x)
print('------------------------------')

# LEN method

string = 'HELLO WORLD'
listy = [1, 32, 78, 99]
my_tuple = (3, 4, 5)
print(len(string))
print(string.__len__())
print(len(listy))
print(listy.__len__())
print(len(my_tuple))
print(my_tuple.__len__())
print('------------------------------')
# GET ITEM
your_list = ['a', 'b', 'c', 'd']
print(your_list[0])
print(your_list[2])
print(your_list.__getitem__(0))
print(your_list.__getitem__(2))
print('------------------------------')

class Bookshelf:
    def __init__(self):
        self.content = [[],
                        [],
                        []]

    def add_book(self, location, book):
        self.content[location-1].append(book)

    def remove_book(self, location, book):
        if book in self.content[location-1]:
            self.content[location-1].remove(book)
        else:
            print(f'The book {book} is not in the shelf.')

    def __getitem__(self, location):
        return self.content[location-1]


my_bookshelf = Bookshelf()
my_bookshelf.add_book(1, 'Harry Porter')
my_bookshelf.add_book(1, 'Quantum physics and future')
my_bookshelf.add_book(1,'Fault in our Stars.')

print(my_bookshelf[1])
print(my_bookshelf[2])
print('------------------------------')

class BankAccount:
    def __init__(self, account_number, owner, current_balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = current_balance

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient Amount in account for withdraw.')

    def __bool__(self):
        return self.balance > 0


my_account = BankAccount(767, 'Hasan', 23000)
print(bool(my_account))
my_account.balance = 0
print(bool(my_account))

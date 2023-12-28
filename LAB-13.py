'''
Create a number list class named NUMBERS, to store just number ints or floats. The user of the
NUMBERS class, the driving (main) logic, can add a number in the list, delete, alter, search a
number in the list, print all of them using the iterators. The catch is to internally store all the
numbers in two separate lists for odd and even numbers, but for the users of the NUMBERS class
it is one list. The operations results in many numbers, order them in odd even odd even sequence
until it is possible. The list also provides the index operator to return the number efficiently.
'''


class Numbers:
    def __init__(self):
        self.odd = []
        self.even = []

    def add(self, number):
        if  isinstance(number, int):
            if number % 2:
                self.odd.append(number)
            else:
                self.even.append(number)
        elif isinstance(number, float):
            if round(number) % 2:
                self.odd.append(number)
            else:
                self.even.append(number)
        else:
            print("Number neither integer nor float!")
    def search(self, number):
        if number in self.odd or number in self.even:
            print(f"Given Number {number} is in the list")
        else:
            print("Number not in list")

    def delete(self, number):
        if number in self.odd:
            self.odd.remove(number)
        elif number in self.even:
            self.even.remove(number)
        else:
            print("Number not in list")

    def alter(self, old_number, new_number):
        if old_number in self.odd:
            index = self.odd.index(old_number)
            self.odd[index] = new_number
        elif old_number in self.even:
            index = self.even.index(old_number)
            self.even[index] = new_number
        else:
            print("Number not in list")

    def complete_list(self):
        complete_list = []
        for i,j in zip(self.odd, self.even):
            complete_list.append(i)
            complete_list.append(j)
        x = []
        if len(self.odd) != len(self.even):
            if len(self.odd) > len(self.even):
                x = [self.odd[len(self.even):]]
            if len(self.even) > len(self.odd):
                x = [self.even[len(self.odd):]]

        for each in x:
            complete_list.append(each)
        return complete_list

    def odd_even_sequence(self):
        lst = self.complete_list()
        for each in lst:
            print(each, end = ", ")
        return

    def __str__(self):
        lst = self.complete_list()
        return f'The numbers are as follows: {lst}'

    def __getitem__(self, index):
        lst = self.complete_list()
        return lst[index]

    def __setitem__(self, index, value):
        lst = self.complete_list()
        x = lst[index]
        if x in self.odd:
            index = self.odd.index(x)
            self.odd[index] = value
        elif x in self.even:
            index = self.even.index(x)
            self.even[index] = value
        else:
            print("Number not in list")

    def __len__(self):
        lst = self.complete_list()
        return len(lst)

    def __iter__(self):
        self._iter_index = 0
        self._iter_list = self.complete_list()
        return self

    def __next__(self):
        if self._iter_index < len(self._iter_list):
            result = self._iter_list[self._iter_index]
            self._iter_index += 1
            return result
        else:
            raise StopIteration

    def __reversed__(self):
        return reversed(self.complete_list())


def main():
    numbers = Numbers()
    # Adding a few numbers
    numbers.add(1)
    numbers.add(2)
    numbers.add(3)
    numbers.add(4)
    numbers.add(5)
    numbers.add(6)
    # Using the search function
    numbers.search(3)
    # Using the delete function
    numbers.delete(2)
    # Using the alter function
    numbers.alter(1, 7)
    # Using the complete_list function
    print(numbers.complete_list())
    # Using the odd_even_sequence function
    numbers.odd_even_sequence()
    # Using the __str__ function
    print(numbers)
    # Using the __getitem__ function
    print(numbers[0])
    numbers[0] = 8
    print(numbers[0])
    print(len(numbers))
    for number in numbers:
        print(number)
    for number in reversed(numbers):
        print(number)
if __name__ == "__main__":
    main()





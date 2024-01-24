class Movies:
    def __init__(self, name, rating):
        self._name = name
        self._rating = rating

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print('Enter Valid Name.')

    @property
    def rating(self):
        print('Getter activated')
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        print('Setter activated')
        if 5 >= new_rating >= 0 and isinstance(new_rating, (int or float)):
            self._rating = new_rating
        else:
            print('Enter Valid New Ratings.')


fav_movie = Movies('Inception', 4.7)
print(fav_movie.rating)
fav_movie.rating = 5
print(fav_movie.rating)


# Example 2
class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        print('Getter activated')
        return self._items

    @items.setter
    def items(self, new_items):
        print('Setter activated')
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Enter valid list of item.')


my_bag = Backpack()
print(my_bag.items)
my_bag.items = ['water-bottle', 'stationary', 'books']
print(my_bag.items)


# Example 3
class Bouncyballs:


    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int):
            self._price = new_price
        else:
            print('Enter valid price')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, (int or float)):
            self._size = new_size
        else:
            print('Enter valid size')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str):
            self._brand = new_brand
        else:
            print('Enter valid brand')

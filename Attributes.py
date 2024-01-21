class Movie:         # class name
    id = 1           # attribute

    def __init__(self, name, genre, release_year):        # init function
        self.name = name
        self.genre = genre
        self.release_year = release_year
        self.id = Movie.id
        Movie.id += 1                                 # increment in attribute


my_fav = Movie("Shutter Island", "Thriller", 2016)
your_fav = Movie("La La Land", "Romance", 2018)

print(my_fav.id)                    # accessing attributes
print(your_fav.id)

my_fav.id = 99              # changing or modifying attribute value a single instance
print(my_fav.id)


# EXAMPLE 2 OF MODIFYING ATTRIBUTE
class Backpack:
    max_bags = 10
    id = 1

    def __init__(self, color):
        self.id = Backpack.id
        self.color = color
        Backpack.id += 1


bag = Backpack("BLACK")
print(Backpack.max_bags)
print(bag.max_bags)

Backpack.max_bags = 20       # value of attribute is modified from 10 to 20
print(Backpack.max_bags)
print(bag.max_bags)

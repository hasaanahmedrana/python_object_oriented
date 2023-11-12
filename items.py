class Items:
    total= 0
    def __init__(self,product,rate,quantity):
        self.__product = product
        self.__rate = rate
        self.__quantity = quantity
        Items.total += rate*quantity
        self.__str__()
    def __str__(self):
        return (f"{self.__product}\t{self.__rate}\t    {self.__quantity}\t{Items.total}")


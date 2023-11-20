#-----------------ADDRESS CLASS---------------------

class Address:
    """
    The Address class represents a address with house number, street number, area, city, and province.
    Attributes:
        house_no (int).
        street_no (int)
        area (str).
        city (str).
        province (str).
    Methods:
        __init__(self, house_no, street_no, area, city, province): Initializes an Address object with the provided values.
        __str__(self): Returns a string representation of the address.
    """
    def __init__(self,house_no,street_no,area,city,province,type):
        self.house_no = house_no
        self.street_no =  street_no
        self.area = area
        self.city = city
        self.province = province
        self.type = type
        self.__str__()

    @property
    def house_no(self):
        return self.__house_no
    @house_no.setter
    def house_no(self,new):
        self.__house_no = new
    @property
    def street_no(self):
        return self.__street_no
    @street_no.setter
    def street_no(self, new):
        self.__street_no = new
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new):
        self.__city = new
    @property
    def province(self):
        return self.__province
    @province.setter
    def province(self, new):
        self.__province = new

    def __str__(self):
        if self.type=='H':
            return (f"House no. {self.house_no}, street no. {self.street_no}, {self.area.capitalize()}, {self.city.capitalize()}, {self.province.capitalize()}")
        return (f"Shop no. {self.house_no}, street no. {self.street_no}, {self.area.capitalize()}, {self.city.capitalize()}, {self.province.capitalize()}")        


#-------------------ITEM ON BILL CLASS----------------------

class Items:
    """
    The Items class represents products, their rates, and quantities.
    Attributes:
        product (str): The name of the product.
        rate (int): The rate of the product.
        quantity (int): The quantity of the product.
    Methods:
        __init__(self, product, rate, quantity): Initializes an Items object with the provided values.
        __str__(self): Returns a  string representation of the product, rate, quantity, and the total amount.
    """
    total= 0
    def __init__(self,product,rate,quantity):
        self.__product = product
        self.__rate = rate
        self.__quantity = quantity
        Items.total += rate*quantity
        self.__str__()
    def __str__(self):
        return (f"{self.__product}\t\t{self.__rate}\t{self.__quantity}\t\t{self.__rate*self.__quantity}")
    
    

# from address import Address
# from items import Items
from datetime import datetime

#---------------------BILL CLASS--------------------------

class Bill:
    SHOP =   '---------------* MOBILO! *-----------------'
    INFO =   '------------* MOBILE CITY *----------------'
    SLOGAN = 'WE DEAL WITH ALL KIND OF MOBILE ACCESSARIES'
    CELL = '09000067578'
    no=0
    SHOP_ADDRESS = Address(12,2,'model town','lahore','punjab','S')
    
    """
    The Bill class represents a customer's bill with customer name, date, and address.
    Attributes:
        name (str), date (str), address (Address)
    class Attributes:
        SHOP (str), INFO (str), SLOGAN (str), CELL (str), no (int), SHOP_ADDRESS (Address)
    Methods:
        __init__(self, name, address): Initializes a Bill object with the customer's name and address.
        __str__(self): Returns a formatted string representation of the bill.
        info(cls): Class method to display shop information.
    """
    def __init__(self,name,address):
        self.name = name
        self.date = datetime.now().strftime('%d-%b-%Y')
        self.address = address
        Bill.no+=1
        self.__str__()

    def __str__(self):
        result = f"Date: {self.date}\n"
        result += f"Customer Name: {self.name}\n"
        result += f"Customer address: {self.address}\n"
        return result

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new):
        if isinstance(new, str):
            self.__name = new
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        if isinstance(address, list) and len(address) == 6:
            self.__address = Address(address[0], address[1], address[2], address[3], address[4],address[5])
    @classmethod
    def info(cls):
        print(cls.SHOP)
        print(cls.INFO)
        print(cls.SLOGAN)
        print('Contact us: ', cls.CELL)
        print('No: ', cls.no)
        print()
        
        
#-----------------------BILL. TEST CLASS-------------------------

def main():
    x = Bill('Hasaan rana ', [23, 2, 'Muslim Town', 'Lahore', 'Punjab', 'H'])
    Bill.info()
    p1 = Items('Mobile', 50000, 2)
    p2 = Items('Sim ', 300, 5)
    p3 = Items('Charger', 500, 12)
    p4 =Items('Remote', 1250, 10)
    print(x)
    print('-------------------INVOICE--------------------\n')
    print('PRODUCT:\tRATE:\tQUANTITY:\tAMOUNT:')
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print('\nSIGNATURE: ____________  \t\t''TOTAL:', Items.total,'\n')
    print(Bill.SHOP_ADDRESS)
main()

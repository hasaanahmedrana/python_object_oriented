from address import Address
from datetime import datetime
from items import Items
class Bill:
    SHOP =   '---------------* MOBILO! *-----------------'
    INFO =   '------------* MOBILE CITY *----------------'
    SLOGAN = 'WE DEAL WITH ALL KIND OF MOBILE ACCESSARIES'
    CELL = '09000067578'
    no=0
    SHOP_ADDRESS = Address(12,2,'model town','lahore','punjab')
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
        if isinstance(new,str):
            self.__name = new
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,address):
        if isinstance(address,list) and len(address)==5:
            self.__address = Address(address[0],address[1],address[2],address[3],address[4])
    @classmethod
    def info(cls):
        print(cls.SHOP)
        print(cls.INFO)
        print(cls.SLOGAN)
        print('Contact us: ',cls.CELL)
        print('No: ',cls.no)
        print()

def main():
    total=0
    x = Bill('Hasaan rana ',[23,2,'Muslim Town','Lahore','Punjab'])
    Bill.info()
    p1= Items('Mobile',50000,2)
    p2= Items('Sim ',300,5)
    p3= Items('Charger',500,12)
    p4 =Items('Remote',1250,10)
    print(x)
    print('PRODUCT:\tRATE:\tQUANTITY:\tAMOUNT:')
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print('TOTAL:',Items.total)
main()

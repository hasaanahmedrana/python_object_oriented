from datetime import datetime
class Items:
    def __init__(self,rate,particulars,qty): #items class
        self.rate = rate
        self.particulars = particulars
        self.qty = qty
        return
    @property
    def rate(self):
        return self.__rate
    @rate.setter
    def rate(self,d):
        self.__rate = d
    @property
    def particulars(self):
        return self.__particulars
    @particulars.setter
    def particulars(self,d):
        self.__particulars = d
    @property
    def qty(self):
        return self.__qty
    @qty.setter
    def qty(self,d):
        self.__qty = d
    def __str__(self):
        s = ''
        s+= str(self.rate) + '\t\t' + str(self.particulars) +'\t\t' +str(self.qty) + '\t\t'+str(self.rate*self.qty)
        return s



class Address:
    def __init__(self,house,street,town,city): #address class
        self.house = house
        self.street = street
        self.town = town
        self.city = city
        return
    @property
    def house(self):
        return self.__house
    @house.setter
    def house(self,d):
        self.__house = d
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self,d):
        self.__street = d 
    
    @property
    def town(self):
        return self.__town
    @town.setter
    def town(self,d):
        self.__town = d
    @property
    def city(self):
        return self.__city
    @city.setter
    def city (self,d):
        self.__city = d
    def __str__(self):
        s = ''
        s += str(self.house)+', '+str(self.street)+', '+str(self.town)+', '+str(self.city)+'.'
        return s
    
    
class Bill:
    def __init__(self,no,name,date,address,items): #bill class
        self.no = no
        self.name = name
        self.date = date
        self.address = address
        self.items = items
        return
    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self,d):
        self.__no = d
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,d):
        self.__name =d
    @property
    def date(self):
        return self.__date
    @date.setter
    def date (self,d):
        self.__date = d
    @property
    def address(self):
        return (self.__address)
    @address.setter
    def address(self,d):
        self.__address =d
    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self,d):
        self.__items =d
    def __str__(self):
        total=0
        s=''
        s += 'MOBILO'
        s += '\n'
        s += 'Mobile City'
        s += '\n'
        s += 'Deals in all kinds of mobile sets and accessories'
        s += '\n'
        s += 'Cell No: 0315-0000000'
        s += '\n'
        s += 'CASHMEMO'
        s += '\n'
        s += 'No: '+str(self.no)+'\n'
        s += 'Date: ' +str(self.date.strftime('%d-%b-%Y'))+'\n'
        s += 'Name : ' +str(self.name)+'\n'
        s += 'Address:' + str(self.address) +'\n'
        s += 'Qty'+'\t\t'+'Particulars'+'\t'+'RATE'+'\t\t'+'Amount'+'\n'
        for i in range (len(self.items)):
            total += self.items[i].qty*self.items[i].rate
            s += str(self.items[i])+'\n'
        s += '\t\t\t\t\t\t' +   'TOTAL:'+str(total) +'\n'
        s += 'Signature:___________________'+'\n'
        s += 'Address: Basement # 2, Allahwala Plaza, Markaz K8, Islamabad'
        return s
    
    
    
def main():
    bill = Bill(723428847,'Areeba',datetime.now(),Address('house no 72','street no 25','bnu','lhr'),[Items(100,'Mouse',2),Items(200,'laptop',3),Items(500,'usb',1)])
    print(bill)
if __name__=='__main__':
    main()

class Address:
    def __init__(self,house_no,street_no,area,city,province):
        self.house_no = house_no
        self.street_no =  street_no
        self.area = area
        self.city = city
        self.province = province
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
    def street_no(self,new):
        self.__street_no = new
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,new):
        self.__city = new
    @property
    def province(self):
        return self.__province
    @province.setter
    def province(self,new):
        self.__province = new

    def __str__(self):
        return (f"House no. {self.house_no}, street no. {self.street_no}, {self.area.capitalize()}, {self.city.capitalize()}, {self.province.capitalize()}")



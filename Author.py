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
        genders = ('M','F','O')  #M-male, F-female, O-others
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
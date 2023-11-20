class Polynomial:
    
    def __new__(cls, deg=0,coffie=[],var='x'):     
        '''Construct a new Polynomial'''
        new_object = super().__new__(cls)
        return new_object
    def __init__(self, variable, coefficient):
        '''Initialize a new Polynomial'''
        self.variable = variable
        self.degree = len(coefficient)-1
        self.coefficient = coefficient

    @property
    def variable(self):
        '''Return the variable'''
        return self.__variable
    @variable.setter
    def variable(self, new):
        '''Set the variable'''
        if isinstance(new, str) and len(new)==1 and new.isalpha():
            self.__variable = new
        else:
            print('Plaase Enter Valid Variable For Polynomial!')
    @property
    def coefficient(self):
        ''' Return The coefficient'''
        return self.__coefficient
    @coefficient.setter
    def coefficient(self, new):
        ''' Set the coefficient'''
        if isinstance(new,list) and len(new)>=1:
            self.__coefficient = new
        else:
            print('Please Enter Valid Coefficients(in list form)!')
        
    @staticmethod
    def  resolving(self, variable_value):
        '''evaluate the polynomial for giving variable value.'''
        y = self.coefficient
        y = [(variable_value**(self.degree-i))*y[i] for i in range(len(y))]
        return sum(y)

    def __str__(self):
        '''Returns polynomial representation'''
        result = ''
        for i in range(self.degree+1):
            if i>0:
                sign =' + ' if self.coefficient[i]>0 else ' - '
                result += sign
            result += str(self.coefficient[i])
            if i!=self.degree:
                result += self.variable
                result += '^'
                result += str(self.degree-i)
        return result
    
    def __add__(p,q):
        '''Add a polynomial to the another'''
        if isinstance(p,Polynomial) and isinstance(q,Polynomial):
            if len(p.coefficient)==len(q.coefficient) and p.variable==q.variable:
                result =[]
                for i,j in zip(p.coefficient,q.coefficient):
                    result.append(i+j)
                return Polynomial(p.variable,result)
            elif len(p.coefficient)!=len(q.coefficient) and p.variable==q.variable:
                # Setting x to polynomial with higher degree and y with lower degree.
                if len(p.coefficient)>len(q.coefficient):
                    x,y = p.coefficient,q.coefficient
                else :
                    x,y = q.coefficient,p.coefficient
                result = x
                for i in range(len(y)):
                    n = -(i+1)
                    result[n] += y[n]
                return Polynomial(p.variable,result)            
            else:
                raise Exception ("Polynomial's variable not matching!")
        else:
            raise ValueError('Polynomial can only be added into a Polynomial')        
    

    def __sub__(p,q):
        '''Subtracts a Polynomial from other Polynomials'''
        if len(p.coefficient)==len(q.coefficient) and p.variable==q.variable:
            result =[]
            for i,j in zip(p.coefficient,q.coefficient):
                result.append(i-j)
            return Polynomial(p.variable,result)
        elif len(p.coefficient)!=len(q.coefficient) and p.variable==q.variable:
            # Setting x to polynomial with higher degree and y with lower degree.
            if len(p.coefficient)>len(q.coefficient):
                x,y = p.coefficient,q.coefficient
            else :
                x,y = q.coefficient,p.coefficient
            result = x
            for i in range(len(y)):
                n = -(i+1)
                result[n] += -y[n]
            return Polynomial(p.variable,result)            
        else:
            raise Exception ("Polynomial's variable not matching!")
        
    def __eq__(self,other):
        '''Determines whether two polynomials are equal'''
        return self.coefficient == other.coefficient

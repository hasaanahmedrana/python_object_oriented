class polynomial:

    def __new__(cls, deg=0,coffie=[],var='x'):
        print("Creating polynomial")
        obj = super().__new__(cls)
        return obj

    def __init__(self, degree=0, coffie=[], variable='x'):
        self.degree = degree
        self.coffie = coffie
        self.variable = variable

    @property
    def degree(self):
        return self.__degree
    @degree.setter
    def degree(self, new):
        self.__degree = new
    @property
    def coffie(self):
        return self.__coffie
    @coffie.setter
    def coffie(self, new):
        self.__coffie = new
    @property
    def variable(self):
        return self.__variable
    @variable.setter
    def variable(self, new):
        self.__variable = new

    def __str__(self):
        out = ''
        for k in range(self.degree):
            if self.coffie[k] >= 0:
                if k != 0:
                    out += ' + '
                out += str(self.coffie[k]) + str(self.variable)+'^' + str(self.degree- k)
            else:
                out +=' '+ str(self.coffie[k]) + str(self.variable)+'^' + str(self.degree- k)
        if self.coffie[-1] >= 0:
            out +=' +' + str(self.coffie[-1])
        else:
            out +=''+ str(self.coffie[-1])
        return out

    @staticmethod
    def add(p1, p2):
        result = polynomial()
        if p1.degree == p2.degree:
            result.degree = p1.degree
            result.variable = p1.variable
            result.coffie = [0]*(p1.degree+1)
            for i in range(p1.degree+1):
                result.variables[i] = p1.variables[i] + p2.variables[i]
        elif p1.degree>p2.degree:
            result.degree = p1.degree
            result.coffie = [0]*(p1.degree+1)
            result.variable = p1.variable
            differ = p1.degree-p2.degree
            for i in range(differ):
                result.coffie[i] = p1.coffie[i]
            for i in range(p2.degree+1):
                result.coffie[differ+i] = p1.coffie[differ+i] + p2.coffie[i]
        elif p2.degree>p1.degree:
            result.degree = p2.degree
            result.coffie = [0]*(p2.degree+1)
            result.variable = p2.variable
            differ = p2.degree-p1.degree
            for i in range(differ):
                result.coffie[i] = p2.coffie[i]
            for i in range(p1.degree+1):
                result.coffie[differ+i] = p1.coffie[i] + p2.coffie[differ+i]
        return result

    @staticmethod
    def subtract(p1, p2):
        result = polynomial()
        if p1.degree == p2.degree:
            result.degree = p1.degree
            result.variable = p1.variable
            result.coffie = [0]*(p1.degree+1)
            for i in range(result.degree):
                result.coffie[i] = p1.coffie[i]-p2.degree[i]
        elif p1.degree>p2.degree:
            result.degree = p1.degree
            result.coffie = [0]*(p1.degree+1)
            result.variable = p1.variable
            differ = p1.degree-p2.degree
            for i in range(result.degree):
                result.coffie[i] = p1.coffie[i]
            for j in range(result.degree):
                result.coffie[differ+j] = p1.coffie[differ+j]-p2.coffie[j]
        else:
            result.degree = p2.degree
            result.coffie = [0]*(p2.degree+1)
            result.variable = p2.variable
            differ = p2.degree - p1.degree
            for i in range(differ):
                result.coffie[i] = p2.coffie[i]
            for j in range(result.degree):
                result.coffie[differ+j] = p2.coffie[differ+j] - p1.coffie[j]
        return result

    @staticmethod
    def evaluate(p,x):
        result = 0
        power = p.degree
        for i in range(p.degree+1):
            result += p.coffie[i]*(x**power)
            power -= 1
        return result


from polynomial import Polynomial
def main():
    p = Polynomial('x', [4,4,4,4])
    print('Polynomial#1: ' ,p)
    q = Polynomial('x', [1,2,3])
    print('Polynomial#1: ' ,q)
    r = Polynomial('x', [1,2,3])
    print('Polynomial#3: ' ,r)
    print('Evualating Polynomial#1 when x=2: ',Polynomial.resolving(p,2))
    print('Evualating Polynomial#1 when x=3: ',Polynomial.resolving(p,3))
    print('Adding both polynomials: ',p+q)
    print('Subtracting both polynomials: ',p-q)
    print('Is p equals to q:',p==q)
    print('Is q equals to r:',q==r)
if __name__ == '__main__':
    main()

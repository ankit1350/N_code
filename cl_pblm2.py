class complex:
    def __init__(self,r=0.0,i=0.0):
        self.__real=r
        self.__imag=i
    def __eq__(self,other):
        if self.__real==other.__real and self.__imag==other.__imag:
            return True
        else:
            return False
        
c1=complex(1.1,0.3)
c2=complex(1.1,0.3)
c3=c1
if c1==c2:
    print('attributes of c1 and c2 are equal')
else:
    print('attributes of c1 and c2 are not equal')
if type(c1)==type(c3):
    print('c1 and c3 are of same type')
else:
    print('c1 and c3 are of different type.')
if c1 is c3:
    print('c1 and c3 are pointing to the same object')
else:
    print('c1 and c3 are not pointing to the same object')
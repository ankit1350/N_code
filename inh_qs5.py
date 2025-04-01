class complex:
    def __init__(self,real.imag):
        self.real=real
        self.imag=imag

    def __add__(self,other):
        return complex(self.real+other.real,self.imag+other.imag)
    
    def __mul__(self,other):
        return complex(self.real*other.real-self.real.imag*other.imag
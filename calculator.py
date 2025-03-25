class calculator:
    def __init__(self):
        self.result=0
    def add(self,a,b):
        self.result=a+b
        return self.result
    def sub (self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def square(self,a):
        return a*a
    
cal=calculator()
print(cal.add(1,2))
print(cal.sub(342,34))
print(cal.mul(23,2))
print(cal.div(23,2))
print(cal.__init__)
print(cal.square(3))
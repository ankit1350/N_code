class Date:
    def __init__(self,d,m,y):
        self.day,self.month,self.year=d,m,y
    def __eq__(self,other):
        if self.day==other.day and self.month==other.month and self.year==other.yr:
            return True
        else:
            return False
d1=Date(17,11,98)
d2=Date(19,10,91)
print(id(d1))
print(id(d2))
print(d1==d2)
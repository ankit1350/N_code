class shape:
    pass
class rectangle(shape):
    pass
class circle(shape):
    pass
s=shape()
c=circle()
print(isinstance(s,shape))
print(isinstance(s,circle))
print(isinstance(s,rectangle))
print(issubclass(rectangle,shape))
print(issubclass(circle,shape))
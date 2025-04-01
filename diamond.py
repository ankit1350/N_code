# Diamond Problem in Multiple Inheritance

class A:
    def display(self):
        print("Display method from class A")

class B(A):
    def display(self):
        print("Display method from class B")
        #classes B and C derived from A, so we can call A's display method
class C(A):
    def display(self):
        print("Display method from class C")

class D(B, C):
    def display(self):
        super().display()
        B.display(self)
        C.display(self)
        print(D.__mro__)

# Creating an object of class D
obj = D()
obj.display()  # Resolves using Method Resolution Order (MRO)
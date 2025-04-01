class animal:
    pass
class pet(animal):
    pass
class dog(pet):
     def bark(self):
         print("bark! bark!")
     
d=dog()
d.bark()
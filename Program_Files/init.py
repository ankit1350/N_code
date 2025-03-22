class Employee():
    def set_data(self,n,a):      #set data used to modify an alreaady initialized object.
        self.__name=n
        self.__age=a
    
    def display_data(self):
        print(self.__name,self.__age)

    def __init__(self,n='',a=0): #__init__() is  called only once durig entire lifetime of an object. it is used to initialize the object
        self.__name=n
        self.__age=a

    def __del__(self): #__del__() method gets called automatically when an object goes out of scope.
        print('Deleting object'+str(self))

e1=Employee() #whenever an object is created , space is allocated in the memory for it. then the address of the object is passed to __init()
e1.set_data('John',30) #__init__() doesn't have any return type
e1.display_data()
e2=Employee('Smith',35)
e2.display_data()
e1=None
e2=None
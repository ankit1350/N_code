class Employee:          #defining the class
    def set_data(self,n,a,s):   #defining the first method of Employee class
        self.name=n     #self=contains the address of of the object. using this  address we indicate which object's instance daata we wish to woek with.
        self.age=a          #any name other than the self can be used but it is a convention to use self
        self.salary=s       
    def display_data(self):
        print(self.name,self.age,self.salary)

e1=Employee()
e1.set_data('ramesh',23,23222)    #instance data is written in the object e1
e1.display_data()             #displaying the instance data of object e1
e2=Employee()                #e1 and e2 are two nameless objects of Employee class
e2.set_data('suresh',24,43552)  #both the employee objects have different instance data
e2.display_data()    #we accessed instance methods outside the class using the object of the class
e3=Employee()        #here we are accessing the the instance data name,age,salary of the object e3
e3.name='rajesh'
e3.age=25
e3.salary=987986
e3.display_data()          #
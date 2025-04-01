class Employee:
    def salary(self,salary):
        self.salary=salary
        return self.salary
    def increment(self,increment):
        self.increment=increment
        print(f"the increment salary is {self.salary+self.increment}")

e=Employee()
e.salary(80000)
e.increment(5000)
class Company:
    def set_name(self, name):
        self.name = name
        print(f"Company name is {self.name}")

class Employee(Company):
    def set_details(self, name, salary):
        self.name = name  # Assign to instance attribute
        self.salary = salary  # Assign to instance attribute
        print(f"The employee name is {self.name} and the salary is {self.salary}")

# Creating instances and using methods
a = Company()
a.set_name("Google")

b = Employee()
b.set_details("Sai", 100000)


# This script demonstrates the concept of multiple inheritance in Python by defining three classes: 
# `Product`, `Sales`, and `HardwareItem`. The `HardwareItem` class inherits from both `Product` and `Sales`.

class Product:
    """
    Represents a product with attributes for title and price.
    Prompts the user to input the title and price of the product during initialization.
    Contains a `display` method to print the product details.
    """
    def __init__(self):
        self.__title = input("Enter title: ")
        self.__price = input("Enter price: ")

    def display(self):
        """
        Prints the product details.
        """
        print("Title:", self.__title)
        print("Price:", self.__price)

class Sales:
    """
    Represents sales data with an attribute for sales figures.
    Prompts the user to input sales figures as a comma-separated list during initialization.
    Contains a `display` method to print the sales figures.
    """
    def __init__(self):
        self.__sales_figures = [int(x) for x in input("Enter sales figures (comma-separated): ").split(",")]

    def display(self):
        """
        Prints the sales figures.
        """
        print("Sales figures:", self.__sales_figures)

class HardwareItem(Product, Sales):
    """
    Inherits from both `Product` and `Sales` classes.
    Represents a hardware item with additional attributes for category and OEM (Original Equipment Manufacturer).
    Prompts the user to input the category and OEM during initialization.
    Overrides the `display` method to display details from both parent classes (`Product` and `Sales`) 
    along with its own attributes.
    """
    def __init__(self):
        # Initialize Product attributes
        Product.__init__(self)
        # Initialize Sales attributes
        Sales.__init__(self)
        # Additional attributes for HardwareItem
        self._category = input("Enter category: ")  # Making it protected (single underscore)
        self._oem = input("Enter OEM: ")

    def display(self):
        """
        Prints the details of the hardware item, including product details, sales figures, 
        and its own attributes (category and OEM).
        """
        Product.display(self)
        Sales.display(self)
        print("Category:", self._category)
        print("OEM:", self._oem)

# Creating HardwareItem objects and displaying data
hw1 = HardwareItem()
hw1.display()

hw2 = HardwareItem()
hw2.display()  def __init__(self):
        self.__title = input("Enter title: ")
        self.__price = input("Enter price: ")

 
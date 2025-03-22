class Number:
    def set_number(self,n):
        self.__num=n
    def get__number(self):
        return self.__num
    def print_number(self):
        print(self.__num)

a=Number()
a.set_number(25)
a.get__number()
a.print_number()
        

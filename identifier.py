def printit():
    print('Opener')

class Message:
    def display(self,msg):      #this is an instance method so we need to pass self as a parameter
        #self is a reference to the instance of the class
        printit()
        print(msg)
    
    def show():    #it's a class method so we don't need to pass self as a parameter 
        printit()
        print('hello')
        

printit()
m=Message()
m.display('good morning')
Message.show()    #m.show() will not work because it's a class method and it can't be called by an instaance of the class
#Message.show(m)    #this will work but it's not a good practice to call a class method like this
        
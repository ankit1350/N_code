def myfunc():
    print("hello world")

if __name__=="__main__":   #if this code is directly executed by running the file it is present in then this code will run
    print("we are directly running this file.")
    myfunc()
    print(__name__)
     
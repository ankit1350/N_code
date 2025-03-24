with open ("message.txt","w")as f:
    f.write("the class describe two things\n"
    "1. the class is a blueprint for creating objects\n"
    "2. the class is a blueprint for creating objects\n"
    )
with open ("message.txt","rb")as f:
    print(f.read())
    print(f.tell())
    print(f.readline())
    print(f.seek(50,0))
    
    print(f.read())
    print(f.seek(131,0))
    print(f.seek(0,2))
    print(f.seek(61,1))
    print(f.seek(61,2))

with open ("message.txt","a")as f:
    f.write("ak")
    print(f.read)
    print(f.seek(0,0))
import  random                           #importing random module
'''1=snake
-1=water
0=gun'''

computer=random.choice([1,-1,0])     #generating random number for computer by using choice function
youStr=input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
reversedDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youStr]

print(f"you chose {reversedDict[you]}\n computer chose {reversedDict[computer]}")

if (computer==you):
    print("it's a draw.")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    else:
        print("something went wrong")
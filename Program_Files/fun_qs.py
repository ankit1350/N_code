#1st question
'''def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
print(f"the greatest of the three numbers is {greatest(a,b,c)}")'''

'''#2nd question
def convert(c):
    return 9*(c)/5+32
c=int(input("enter the temperature in celsius:"))
print(f"the temperature in fahrenheit is {convert(c)}")'''

'''#3rd question
print("ankit",end="")

print("kumar")

#4th question
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
n=int(input("enter the number:"))
print(f"the sum of first {n} natural numbers is {sum(n)}")'''


'''#5th question

def pattern(n):
    if n==0:
        return        #to stop condition at that point
    print("*"*n)
    return pattern(n-1)
n=int(input("enter the number:"))
pattern(n)'''
'''
#6th question
def convert(i):
    if i==0:
        return
    return 2.54*i
i=int(input("enter the number:"))
print(convert(i))'''

'''#7th question
def table(n ):
    for  i  in range(1,11):
        print(f"{n}X{i}={n*i}")

n=int(input("enter the number:"))
print(table(n))
    '''
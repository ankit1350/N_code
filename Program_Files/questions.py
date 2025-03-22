'''#1. to print the table of a number
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    i+=1


#2nd question  same question as above but using while loop
n=int(input())
i=1
while(i<=10):
    print(f"{n} x {i} = {n*i}")
    i+=1

#3. check whether a number is prime or not
n=int(input())
for i in range(2,n):
    if n%i==0:
        print("the number is not prime.")
        break
else:
    print("the number is a prime number.")


#4. to find sum of first n natural numbers.abs
n=int(input())
i=0
sum=0
while (i<=n):
    sum+=i
    i+=1
print(sum)


#5. to find the factorial of a number.
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    i+=1
print(f"the factorial of {n}is{fact}")'''




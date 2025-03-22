#1. to print the star pattern
'''n=int(input("enter the number:"))
for i in range(1,n+1):           #n+1 to work till n.
    print(" " *(n-i),end="")     #printing spaces  present before the star. observe the pattern.
    print("*" *(2*i-1),end="")   #printing the stars in the same line applying the formula for odd numbers
    print("")                    #printng blank for a new line
''''''

    #2. same question with different pattern
n=int(input("enter the number:" ))
for i in range(1,n+1):                        #this loop print the stars as in natural number form.
        print("*"*i)
       ''''''
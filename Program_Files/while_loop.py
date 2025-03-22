#list using while loop
#write all the elements respectively 
#this program works as the value of i is less than the length of the list it will print the value of the list at that index and 
#then increment the value of i by 1 and then again check the condition and if it is true then again print the value of the list at
#that index and so on.

l=[True,"sanskriti","ankit",234]
i=0
while (i<len(l)):
    print(l[i])
    i=i+1   
l=[1,2,3,4,5]
#using for loop simple method
sq_list=[]
for i in l:
    sq_list.append(i**2)

print(sq_list)

#using map function:
sq_list=list(map(lambda x:x**2,l))
print(sq_list)

#using the list comprehension method:
sq_list=[i**2 for i  in l]
print(sq_list)
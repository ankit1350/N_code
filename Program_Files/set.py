d={}  #do  not make an empty set1 like this as this is an empty dictionary
print(type(d))
e=set() #this is an empty set1
print(type(e))
set1={1,3,4}
print (sum(set1))
print(set1)
print(len(set1))
set2={34,2432,"sanskriti"}
print(set1.union(set2)) 
print(set1.intersection(set2))
print(set1.add(900))
# set3={24,34,"ankita",[4,5]}  #the inside list is immutable so it will give an error 
set4={24,34,"ankita",(4,5)}  #the inside inside tuple is immutable so it will not give an error
print(set4)

print(set1|set2)  #this is the union of the two sets
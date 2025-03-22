tuple1=(1,2,3,4,5,)
tuple2=(6,7,8,9,10)
print(tuple1+tuple2)
new=tuple(reversed(tuple1))
print(new)
print(tuple1[2:4])
print(tuple2[:4])
print(tuple2[-3:-1])
print(tuple1[1:5:2])
print(tuple2[1:3])
print(len(tuple1))
concated=tuple1+tuple2
print(concated)
print(tuple2.index(8))
print(tuple1.count(3))
print(9 in tuple1)
first, *middle,last=tuple1 #unpacking
print(first)
print(middle)
print(last)
print(tuple1[::-1])      #reverse: [start:stop:step] step=-1 i.e: go backwards one step
print(tuple1[:-1])
print(tuple1[::])
list=list(tuple1)       #converting tuple to list
print(list)
a,b,c,d,e=tuple1   #unpaking tuple1 into a,b,c,d,e
print(b)
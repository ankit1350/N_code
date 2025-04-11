l=[334,345,57,887,4]
index=0

for item in l:
    index+=1
    print(f"the item at index {index} is {item}")

#or we can do this using enumerate function also

for index, item in enumerate(l):
    print(f"the item at index {index} is {item}")
# in this way wwe can get the index and item in one go without using the index variable
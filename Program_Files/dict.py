marks={
    "ankit": 96,
    "rahul":8,
    "shruti":78,
    52:"anshu"
}
print(marks)
marks.update({"ankit":100})  #the one which is already present will be updated and the new one will be added
print(marks.get("ankit"))
print(marks.get("ankit1"))  #this will not give error as it is not  present in the dictionary
print(marks["ankit"])
# print(marks["ankit1"])   #this will give error as it is not present in the dictionary
print(marks.pop("ankit"))  #this will remove the key and value of the key
print(marks)
#!/usr/bin/python3


list = [ 'Python', 265 , 2.2333, 'Mayur', 70.22 ]

print()
print("Type: ", type(list))
print("Value: ", list)
print()


print("Prints length of list: ", len(list))
print()

print("Prints first elemnt of list: ", list[0])
print()

print("Prints elements starting from 3rd position: ", list[2:])
print()

print("Prints elements starting from 1st position to 3rd position: ", list[1:3])
print()

print("Prints list two times: ", list*2)
print()

newList = list + ["Added new element in list"]
print("Prints concatenated list: ", newList)
print()

# update element in list
list[0] = "Python is best"
print("updated list: ", list)


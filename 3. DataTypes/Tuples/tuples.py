#!/usr/bin/python3


tuple_var = ( 'Python', 265 , 2.2333, 'Mayur', 70.22 )

print()
print("Type: ", type(tuple_var))
print("Value: ", tuple_var)
print()


print("Prints length of tuple: ", len(tuple_var))
print()

print("Prints first elemnt of tuple: ", tuple_var[0])
print()

print("Prints elements starting from 3rd position: ", tuple_var[2:])
print()

print("Prints elements starting from 1st position to 3rd position: ", tuple_var[1:3])
print()

print("Prints tuple two times: ", tuple_var*2)
print()

# not concate element in tuple
secondTuple = ("Added new element in list", 10.2)
newTuple = tuple_var + secondTuple
print("Prints concatenated list: ", newTuple)
print()

# not update element in tuple
# tuple_var[0] = "Python is best"
# print("updated tuple: ", tuple_var)


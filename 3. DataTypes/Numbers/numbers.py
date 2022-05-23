#!/usr/bin/python3

print("This is number example")
print()

intType = 10
print("Type: ", type(intType))
print("Value: ", intType)
print()

floatType = 10.50
print("Type: ", type(floatType))
print("Value: ", floatType)
print()

longType = 0xa
print("Type: ", type(longType))
print("Value: ", longType)
print()


complexType = 9.322-36j
print("Type: ", type(complexType))
print("Value: ", complexType)
print()


#delete a reference
var = 10
print("var is present in memory with value: ", var)

del var
print(var) #this line causes an error as we removed reference of var variable
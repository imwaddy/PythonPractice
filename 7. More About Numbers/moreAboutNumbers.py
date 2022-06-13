
#!/usr/bin/python3

intVal = 10
_value = 20

print(intVal)
print(_value)

# del intVal,_value
# print(intVal) #This line shows error
# print(_value)

# Number Type Conversion
convert = "120"

converted = int(convert)

print("Value of convert value: ", convert)
print("Type of convert value: ", type(convert))

print("Type of converted value: ", type(converted))
print("Value of converted value: ", converted)


converted = int(convert, 3)
print("Value of convert value: ", convert)
print("Type of convert value: ", type(convert))

print("Type of converted value: ", type(converted))
print("Value of converted value: ", converted)

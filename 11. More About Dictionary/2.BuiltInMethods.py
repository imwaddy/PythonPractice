#!/usr/bin/python3

print()


# Length Function
dict = {'Name': 'Mayur', 'Age': 27, 'Class': 'First'}
print("Length of Dictionary: ", len(dict))
print()

# Produces a printable string representation of a dictionary
str1 = str(dict)
print("String representation of Dictionary: ", str1)
print("tring representation of Dictionary: ", type(str1))
print()

# Returns list of dictionary dict's keys
keys = dict.keys()
print("Keys of Dictionary: ", keys)
print()

# Returns list of dictionary dict's values
values = dict.values()
print("Values of Dictionary: ", values)
print()


# Removes all elements of dictionary dict
dict.clear()
print("Empty Dictionary: ", dict)
print()

# for more you can practice on https://www.tutorialspoint.com/python3/python_dictionary.htm
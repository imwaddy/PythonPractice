#!/usr/bin/python3

print()

# Each key is separated from its value by a colon (:),
# the items are separated by commas
# the whole thing is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this: {}.

# Keys are unique within a dictionary while values may not be.
# The values of a dictionary can be of any type,
# but the keys must be of an immutable data type such as strings, numbers, or tuples.

dict = {'Name': 'Mayur', 'Age': 27, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print()

# If we try to get element which is not present in dict it will give error
# print ("dict['email']: ", dict['email'])

# updating dictionary
dict['Age'] = 28
dict["Email"] = "mayurwadekar2@gmail.com"  # adds new entry
print("Updated Dictionary : ", dict)
print()


# deleting dictionary elements and dictionary
del dict["Email"]
print("Updated Dictionary : ", dict)
print()

# del dict - deletes dictionary

# Rules
dict = {'Name': 'Mayur', 'Age': 27, 'Class': 'First', 'Class': 'Second'}
print("dict['Class']: ", dict['Class'])
print()

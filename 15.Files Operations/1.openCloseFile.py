#!/usr/bin/python3

# Open a file
fo = open(
    r"/Users/mayurwadekar/PythonPractice/13. Functions/1.functionDefinition.py", "r+", 10)

print("Name of the file: ", fo.name)
print()

print("Closed or not : ", fo.closed)
print()

print("Opening mode : ", fo.mode)
print()

print("Encoding : ", fo.encoding)
print()

# close a file
fo.closed()

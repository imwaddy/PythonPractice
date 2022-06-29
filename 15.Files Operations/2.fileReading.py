#!/usr/bin/python3

# Open a file
fo = open(
    r"/Users/mayurwadekar/PythonPractice/13. Functions/1.functionDefinition.py", "r+", 10)


print(fo.read(16)) # this will set seek pointer to count 16
print()

print(fo.readline()) # It will return whole line
print()

print("Seek pointer : ", fo.tell())

# close a file
fo.close()
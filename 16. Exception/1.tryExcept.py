#!/usr/bin/python3


# try-except
try:
    # Open a file
    fo = open(
        r"/Users/mayurwadekar/PythonPractice/13.Functions/1.functionDefinition.py", "r+", 10)

except:
    print("This is except block, It cathes all exception if not mentioned.")


# try-except
try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")

except IOError as e:  # you can provide multiple exceptions using comma seperation
    print("Error: can\'t find file to read data. ")
    print("String error ", e.args)


# you can provide multiple except blocks
try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")

except FileExistsError:
    print("Error: File not exists")

except IOError:
    print("Error: can\'t find file to read data")

#!/usr/bin/python3

def isAboveZero(value):
    if value < 0:
        raise Exception(value, "Value less than 0")
        # The code below to this would not be executed
        # if we raise the exception
    return value


try:
    l = isAboveZero(-10)
    print("Value = ", l)
except Exception as e:
    print("error in argument", e.args)

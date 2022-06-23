#!/usr/bin/python3

print()

#function definition and function rules(Explain)

# def functionName( [arguments/ paramters] ):
#     docString[optional]
#     No of statements
#     return [optional]

def calculateSum(no1, no2):
    "This function calculates sum of two numbers" #docString
    c = no1 + no2
    return c

a = calculateSum(1,2) # Call a function
print(a)

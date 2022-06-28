#!/usr/bin/python3

print()

# Below is already on tutorialpoints, make understand it
# 1. Lambda forms can take any number of arguments but return just one value in the form of an expression.
# They cannot contain commands or multiple expressions.

# 2. An anonymous function cannot be a direct call to print because lambda requires an expression.

# 3. Lambda functions have their own local namespace and cannot access variables other than those in their parameter
# list and those in the global namespace.


# 4. Although it appears that lambdas are a one-line version of a function,
# they are not equivalent to inline statements in C or C++, whose purpose is to stack allocation by passing function,
# during invocation for performance reasons.

# you can define function like below
# lambda [arg1 [,arg2,.....argn]]:expression

# usage of lambda
add = lambda no1,no2: no1+no2
sum = add(10,20)
print(add(10,20))

# # Proven point #2
# add = lambda no1,no2: print(no1+no2)
# sum = add(10,20)
# print(add(10,20))


cube = lambda no1: no1*no1*no1
print(cube(2))
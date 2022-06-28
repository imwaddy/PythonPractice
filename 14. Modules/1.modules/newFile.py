#!/usr/bin/python3


import mymodule

mymodule.welcome("Alex")
print()

print("Variables in Python Modules: ", mymodule.PI)

print()




# alices

import mymodule as mmod

mmod.welcome("Alex")
print()

print("Variables in Python Modules: ", mmod.PI)

print()


#from keyword

from mymodule import PI as pi
#you can also use * to import all module variables/methods
#eg. from mymodule import *

# pi.welcome("Alex") # returns an error as we only imported a pi variable from mymodule
# print()

print("Variables in Python Modules: ", pi)

print()


#dir function
print(dir(mymodule))
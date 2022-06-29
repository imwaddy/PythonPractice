#!/usr/bin/python3


import os

print("Current working directory; ", os.getcwd()) # current working directory
print()

os.mkdir("newdir") # creates new dir


os.chdir("/usr")
print("Current working directory; ", os.getcwd())
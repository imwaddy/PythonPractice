#!/usr/bin/python3

print()


def printinfo(name, age=90):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# call printinfo function
printinfo(age=50, name="Mayur")
printinfo(name="Mayur")

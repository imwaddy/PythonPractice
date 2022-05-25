#!/usr/bin/python3

a = 10

print()
if a:
    print("In if statement - A is true")
print()

a = 0
if a:
    print("In if statement - A is true")
print("after if statement")
print()

a = 10
if a > 10:
    print("In if statement - A is having value greater than 10")
else:
    print("In else statement - A is having less or equal value than 10")
print()


a = 10
if a >= 10:
    print("A is greater or equal to 10")
    if a > 5:
        print("A is greater than 5")
    else:
        print("A is smaller than 5")
else:
    print("A is less than 10")
print()

a = 100
if a % 2 == 50:
    print("In if statement")
elif a % 3 == 1:
    print("In else if")
    # you can write as many as else-if statement as per your conditions
else: # this is also optional if you don't want to give any by default condition
    print("No condition is true so I'm in else")
print()


a , b = 10, 20

#short hand if
if a < b: print("a is less than b")
print()

#short hand if-else
print("A") if a < b else print("B")
print()
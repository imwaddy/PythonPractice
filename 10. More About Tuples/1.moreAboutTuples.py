#!/usr/bin/python3

print()

# Tuple items are ordered, non-changeable immutable, and allow duplicate values.
#

tup1 = ('physics', 'chemistry', 'physics', 1997, 2000, [10,33,292,], (22,444,53,"Mayur"))
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d" # you can omit parenthisis
tup4 = () #you can also assign empty parenthisis for assigning a blank tuple

print("Mixed Types Elements: ", tup1)
print("Int Types Elements: ", tup2)
print("String Types Elements: ", tup3)
print()

# ---------
print()

tupleEx = ("Jimmy", "Anderson", "Virat", "Kohli", "Abraham", "Benjamin", "Franklin")
print("List Indexing: ", tupleEx[0])

tupleEx2 = tupleEx[0:5]
print("List 2: ", tupleEx2)

# ---------
print()

#delete tuple

# del tupleEx[len(tupleEx)-1] #not valid operation as tuple is immutable
del tupleEx
print("After delete: ", tupleEx) #this will print error
#NameError: name 'tupleEx' is not defined. Did you mean: 'tupleEx2'?

print()
#!/usr/bin/python3

print()

# List items are ordered, changeable, and allow duplicate values.
#

list1 = ['physics', 'chemistry', 1997, 2000, (1, 2, 3,), ["elem1", "elem2"]]
list2 = [5, 4, 3, 2, 1]
list3 = ["a", "b", "c", "d"]

print("Mixed Types Elements: ", list1)
print("Int Types Elements: ", list2)
print("String Types Elements: ", list3)
print()

# ---------
print()

listEx = ["Jimmy", "Anderson", "Virat", "Kohli", "Abraham", "Benjamin", "Franklin"]
print("List Indexing: ", listEx[0])

list2 = listEx[0:5]
print("List 2: ", list2)

# ---------
print()

#updating value

listEx[0] = "Ravi"
listEx[1] = "Shastri"
print("After Update: ", listEx)
print()

# ---------

#delete list element

del listEx[len(listEx)-1]
print("After delete: ", listEx)
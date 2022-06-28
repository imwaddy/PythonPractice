#!/usr/bin/python3

print()


# def printList(list1):
#     print("In Function: Before Value update ", list1)
#     print("In Function: Before Value update ", id(list1))

#     # We are updatung value here
#     list1[2] = "Updated Value"

#     print("In Function: After Value update ", list1)
#     print("In Function: After Value update ", id(list1))


# lst = [10, 20, 30, 40, 50, 60]

# print("Before Value update ", lst)
# print("Before Value update ", id(lst))

# printList(lst)

# print("After Value update ", lst)
# print("After Value update ", id(lst))


# --------------------------------------------------

print()
print()
print()

def printList(list1):
    print("In Function: Before Value update ", list1)
    print("In Function: Before Value update ", id(list1))

    # We are updatung value here
    list1 = ["Updated Value1", "updated value 2"]

    print("In Function: After Value update ", list1)
    print("In Function: After Value update ", id(list1))


lst = [10, 20, 30, 40, 50, 60]

print("Before Value update ", lst)
print("Before Value update ", id(lst))

printList(lst)

print("After Value update ", lst)
print("After Value update ", id(lst))



print()
print()
print()
#!/usr/bin/python3

print()

# len function - Prints length of list
list1 = ['physics', 'chemistry', 1997, 2000, (1, 2, 3,), ["elem1", "elem2"]]
print("Length of string: ", len(list1))
print()

print("Nested Type Tuple element: ", list1[4][2])
print("Nested Type List element: ", list1[5][1])
print()


# Concatenate lists
list1 = ["list1"]
list2 = ["list2"]
print("New List : ", list1+list2)
print()

# Repetation
list1 = ["list1"]
print("Repeatation :", list1*2)
print()


# membership
list1 = ['Cricket', 'Football', "Hockey",
         "Wrestling", "Rugby", "Chess", "Swimming"]
isTrue = "Chess" in list1
print("is Chess in list1 : ", isTrue)
isTrue = "Basketball" in list1
print("is Chess in list1 : ", isTrue)
print()
# membership operator 'not in' opposite of 'in'

# iteration
list1 = ['Cricket', 'Football', "Hockey",
         "Wrestling", "Rugby", "Chess", "Swimming"]
for x in list1:
    print(x, end='\n')

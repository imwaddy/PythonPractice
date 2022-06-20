#!/usr/bin/python3

print()

# len function - Prints length of tuple
tuple1 = ('physics', 'chemistry', 1997, 2000, (1, 2, 3,), ["elem1", "elem2"])
print("Length of string: ", len(tuple1))
print()

print("Nested Type Tuple element: ", tuple1[4][2])
print("Nested Type List element: ", tuple1[5][1])
print()


# Concatenate lists
tuple1 = ("tuple1")
tuple2 = ("tuple2")
print("New tuple : ", tuple1+tuple2)
print()

# Repetation
tuple1 = ("tuple1")
print("Repeatation :", tuple1*2)
print()


# membership
tuple1 = ('Cricket', 'Football', "Hockey",
          "Wrestling", "Rugby", "Chess", "Swimming")
isTrue = "Chess" in tuple1
print("is Chess in tuple1 : ", isTrue)
isTrue = "Basketball" in tuple1
print("is Chess in tuple1 : ", isTrue)
print()
# membership operator 'not in' opposite of 'in'

# iteration
tuple1 = ('Cricket', 'Football', "Hockey",
          "Wrestling", "Rugby", "Chess", "Swimming")
for x in tuple1:
    print(x, end='\n')

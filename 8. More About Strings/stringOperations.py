#!/usr/bin/python3

print()

# concatenation
str1 = "Python"
str2 = "Programming"
space = " "
concatenatedString = str1 + space + str2

print("Concatenated String: ", concatenatedString)
print()

# Repetition - Creates new strings, concatenating multiple copies of the same string
str1 = "CopyMe"
repeatedString = str1 * 2
print("Repeated String: ", repeatedString)
print()

# Slice - Gives the character from the given index
str1 = "CopyMe"
repeatedString = str1[0:4]
print("Repeated String: ", repeatedString)
print()

# Range Slice - Gives the characters from the given range
str1 = "Python Programming"
rangeString = str1[0:6]
print("Range String: ", rangeString)
print()

# Membership - Returns true if a character exists in the given string
str1 = "Python Programming"
isTrue = "a" in str1
print("Is True: ", isTrue)
isTrue = "e" in str1
print("Is True: ", isTrue)
print()

#same in case of not in
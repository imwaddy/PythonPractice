#!/usr/bin/python3

print()


# Capitalize - It returns a copy of the string with only its first character capitalized.
str1 = "chris gayle"
print("Capitalized string: ", str1.capitalize())
print()

# isdigit - Returns true if string contains only digits and false otherwise.
str1 = "10"
print("Is Digit: ", str1.isdigit())
str1 = "1A0"
print("Is Digit: ", str1.isdigit())
print()

# sequence − This is a sequence of the elements to be joined.
s = "-"
seq = ("a", "b", "c")  # This is sequence of strings.
print(s.join(seq))
print()

# Converts all uppercase letters in string to lowercase.
str1 = "MAYUR WADEKAR"
print("Lower: ", str1.lower())
print()


# Converts all lowercase letters in string to uppercase.
str1 = "mayur wadekar"
print("Upper: ", str1.upper())
print()

# The lstrip() method returns a copy of the string in which all chars have been stripped from the beginning of the string
# default whitespace characters
str = "     this is string example....wow!!!"
print(str.lstrip())

str = "*****this is string example....wow!!!*****"
print(str.lstrip('*'))
# rstrip is opposite of lstrip


# for more you can practice on  https://www.tutorialspoint.com/python3/python_strings.htm

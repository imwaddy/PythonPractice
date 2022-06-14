#!/usr/bin/python3

print()

name = "Virat"
surname = "Kohli"
print("My name is %s and surname is %s" % (name, surname))
print()

# %c - Prints a character
print("My name is %s and weight is %c kg!" % (name, "2"))
print()

# %i - signed decimal integer
print("My name is %s and weight is %i kg!" % (name, 21))
print()

# %d - signed decimal integer
print("My name is %s and weight is %d kg!" % (name, 21))
print()

# %u - unsigned decimal integer
print("My name is %s and weight is %u kg!" % (name, -21))
print()

# %o - octal integers
print("My name is %s and weight is %o kg!" % (name, 8))
print()

# %f - float numbers
print("My name is %s and weight is %f kg!" % (name, 8.10))
print()


# %x - lowercase hexadecimal numbers
print("My name is %s and weight is %x kg!" % (name, 10))
print()


# %x - upparcase hexadecimal numbers
print("My name is %s and weight is %X kg!" % (name, 10))
print()

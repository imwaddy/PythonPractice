#!/usr/bin/python3

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print()
print("Bitwise & operator", c)
print()

c = a | b;        # 61 = 0011 1101 
print("Bitwise | operator", c)
print()

c = a ^ b;        # 49 = 0011 0001
print("Bitwise XOR operator", c)
print()

c = ~a;           # -61 = 1100 0011
print("Bitwise bunary 1's operator", c)
print()

c = a << 2;       # 240 = 1111 0000
print("Bitwise shift left operator", c)
print()

c = a >> 2;       # 15 = 0000 1111
print("Bitwise shift right operator", c)
print()
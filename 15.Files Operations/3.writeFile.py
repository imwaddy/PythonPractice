#!/usr/bin/python3

# Open a file
fo = open("welcome.txt", "w+")
fo.write( "My name is Mayur Wadekar. \nWelcome to Python learning..!!\n")

fo.writelines(["Let's learn Python.\n", "And practice it."])

# Close opend file
fo.close()
#!/usr/bin/python3

print()


#Length Function
tuple1 = ('physics', 'chemistry', 'maths')
print ("Length of tuple: ", len(tuple1))

tuple = tuple(range(5)) #creates list of numbers between 0-4
print ("Length of tuple: ", len(tuple))

print()

# max function
tuple1, tuple2 = ('C++',"Java","Python"), (456, 700, 200)
print ("Max value element : ", max(tuple1))
print ("Max value element : ", max(tuple2))
print()


# min function
tuple1, tuple2 = ('C++',"Java","Python"), (456, 700, 200)
print ("Min value element : ", min(tuple1))
print ("Min value element : ", min(tuple2))
print()

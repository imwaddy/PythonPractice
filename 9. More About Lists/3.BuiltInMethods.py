#!/usr/bin/python3

print()


#Length Function
list1 = ['physics', 'chemistry', 'maths']
print (len(list1))

list2 = list(range(5)) #creates list of numbers between 0-4
print (len(list2))

print()

# max function
list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))
print()

# min() function is opposite of max() function

# appends the object to be appended in the list.
list1 = ['Cricket', 'Football', "Hockey",
         "Wrestling", "Rugby", "Chess", "Swimming"]
list1.append("Chess")
print("Appended List: ",list1)


# Inserts object obj into list at offset index
list1.insert(3, "new sports")
print("Inserted Element: ", list1)

#sorts list
list1.sort() # as it does not return new list it operates on same list
print("Sorted List: ", list1)

#reverse sorts list
list1.reverse() # as it does not return new list it operates on same list
print("Reverse Sorted List: ", list1)

# for more you can practice on https://www.tutorialspoint.com/python3/python_lists.htm
#!/usr/bin/python3

print()
# while loop with break
i = 1
while i < 6:
    print(i)
    if i == 1:
        break
    i += 1
print()

# for loop with continue
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "apple":
        continue
    print(f)
print()


# for loop with pass
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "apple":
        # print("Passing the value")
        pass
        print("Passing the value")
    print(f)
print()

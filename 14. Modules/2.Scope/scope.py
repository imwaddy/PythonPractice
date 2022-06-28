#!/usr/bin/python3


# 1. A Python statement can access variables in a local namespace and in the global namespace. 
# If a local and a global variable have the same name, the local variable shadows the global variable.

# 2. Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions.

# 3. Python makes educated guesses on whether variables are local or global. 
# It assumes that any variable assigned a value in a function is local.

# 4. Therefore, in order to assign a value to a global variable within a function, you must first use the global statement.
# The statement global VarName tells Python that VarName is a global variable. Python stops searching the local namespace for the variable.


Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1

print (Money)
AddMoney()
print (Money)
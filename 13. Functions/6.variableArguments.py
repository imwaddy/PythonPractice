
#!/usr/bin/python3

print()


# def functionname([formal_args,] *var_args_tuple ): 
#     "function_docstring"
#     function_suite 
#     return [expression]

def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("First argument is: ", arg1)


    print("Length of varargs : ", len(vartuple))
    for var in vartuple:
        print("Variable arguments: ", var)
    return


# call printinfo function
printinfo(10)
printinfo(70, 60, 50)

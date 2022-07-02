
#!/usr/bin/python3


import os

# try-except
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")

except IOError as e:  # you can provide multiple exceptions using comma seperation
    print("Error: can\'t find file to write data ", e)

else:  # Else block executes only when there is no exception occures
    print("File contents written successfully.")
    fh.close()
    os.remove("testfile")

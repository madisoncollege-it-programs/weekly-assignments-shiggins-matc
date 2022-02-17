#!/usr/bin/env python3
hFile = open("/etc/passwd","r")
strfiletext = hFile.read()
print(type(strfiletext))
print("This file contains this many strings")
print(len(strfiletext))
print ("We would use this read function to tell how many strings are in a file")
hFile.close()
print("")
print("")
hFile = open("/etc/passwd","r")
listfiletext = hFile.readlines()
print(type(listfiletext))
print("this file contains this many lines")
print(len(listfiletext))
print ("we would use this read funtion to count lines in a file")
hFile.close()
print("")
print("")
with open("/etc/passwd","r") as hFile:
    countLines = 0
    try:
        while True:
            countLines += len(next(hFile))
    except StopIteration:
        print("We would use this for large files using looping and iteration")
print(f"the length of the file is: {countLines}")
hFile.close()

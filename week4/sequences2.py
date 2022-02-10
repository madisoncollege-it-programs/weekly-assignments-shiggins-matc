#!usr/bin/env Python3
varString = "Here is a nice string to slice"
varList = ["Here","is","a","nice","list","to","slice"]
print(f"'{varString[3::]}'")
print(f"'{varString[0:3:]}'")
print(f"'{varString[3:12:]}'")
print(f"'{varString[::2]}'")
print(f"'{varString[::-1]}'")
print(f"['{varList[6]}','{varList[5]}','{varList[4]}','{varList[3]}','{varList[2]}','{varList[1]}','{varList[0]}']")
print(f"['{varList[2]}','{varList[1]}','{varList[0]}']")
print(f"['{varList[2]}','{varList[3]}']")
print(f"['{varList[0]}','{varList[3]}','{varList[6]}']")
print(f"['{varList[1]}','{varList[2]}','{varList[3]}','{varList[4]}','{varList[5]}','{varList[6]}']")
for thing in varString:
    print (thing)
for element in varList:
    print (element)

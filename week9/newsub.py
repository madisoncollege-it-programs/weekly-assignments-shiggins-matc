#!usr/bin/env python3
# By: Sean Higgins

import subprocess
myProc = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)

#print(myImp)
myProcString = myProc.stdout.decode()
myProcList = myProc.stdout.decode().split('\n')
#print(myProcList)
#print(myProcString)
for string in myProcList:
    print(string)
mySlice = myProcList[1::]

print(f"The Length is: {len(mySlice)}")

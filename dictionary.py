#!/usr/bin/env python3
myDict = {"server1.testlab.com":"192.168.1.10",
          "server2.testlab.com":"192.168.1.11",
          "server3.testlab.com":"192.168.1.12",
          "server4.testlab.com":"192.168.1.13",
          "server5.testlab.com":"192.168.1.14",
          "server6.testlab.com":"192.168.1.15",
          "server7.testlab.com":"192.168.1.16",
          "server8.testlab.com":"192.168.1.17"}

for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for items in myDict.items():
    print(items)

for key in myDict.keys():
    print(key)
print("Server2 is present")

for key in myDict.keys():
    print(key)
print("Server10 is not present")

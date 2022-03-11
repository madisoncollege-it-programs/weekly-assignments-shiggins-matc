#!/usr/bin/env python3
print("Name: Sean Higgins")

Total = 0
file_name="update-if.txt"
phrase="Whiteland"
phrase2="gmeach18@ed.gov"
phrase3="248.253.63.149"
phrase4="80.222.19.190"
phrase5="Kayley"
phrase6="dcassyqw@microsoft.com"
with open(file_name) as f:
    for i, line in enumerate(f, 0):
        if phrase in line:
            Total = i
        elif phrase2 in line:
            Total += i
        elif phrase3 in line:
            Total += i
        elif phrase4 in line:
            Total += i
        elif phrase5 in line:
            Total += i
        elif phrase6 in line:
            Total += i


print(f"The total is: {Total}")

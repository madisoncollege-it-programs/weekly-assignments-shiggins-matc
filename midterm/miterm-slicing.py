#!/usr/env/bin python3
print("Name: Sean Higgins")

hFile = open("slicing-file.txt","r")
listfiletext = hFile.readlines()
hFile.close()
varA = listfiletext[24:25:1]
varB = listfiletext[2:5:1]
varC = listfiletext[-10:-15:-2]
varD = listfiletext[10:13:1]
varE = listfiletext[-19:-22:-1]

quote = varA + varB + varC + varD + varE
quoteFin = " ".join(quote)

x = quoteFin.replace("\n"," ")
print(x)

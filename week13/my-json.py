import sys
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Creating a parser to add arguments')

parser.add_argument('-ip', action='store', dest='varString', default='8.8.8.8', type=str, help='Enter an ip')
#print((parser.parse_args()).varString)
myInput = input("Input an ip")
url = (f"http://ipinfo.io/{myInput}/json")


# Send the “get” request to the web server
jsonResp = requests.get(url)
# Convert the returned json formatted text to a dictionary
myDict = json.loads(jsonResp.text) 

# for each key in the dictionary print the key and the data
#for key in dictResp.keys():
 #   print(f"{key: <10}:{dictResp[key]: <10}")
for key in myDict.keys():
    print(f'{key: <10}:{myDict[key]: <10}')


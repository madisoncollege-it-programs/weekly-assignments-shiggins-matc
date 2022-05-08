#!/usr/bin/env python3
import requests,json,argparse,socket
parser = argparse.ArgumentParser(description='Creating a parser to add arguements')
parser.add_argument('-i', dest='varString', type=str, help='Enter 1-5')
parser.add_argument('-ip', '--ipaddress', dest='varString2', type=str, help='Enter an IP address')
args = parser.parse_args()
URL= (f'http://{args.varString2}/q{args.varString}')
xVar = args.varString
print("Name: Sean Higgins")
print(URL)
if xVar =="1":
    json_raw = requests.get(URL)
    x = json.dumps(json_raw.text)
    print(f"Answer: {x}")
elif xVar =="2":
    json_raw = requests.get(URL)
    varNew = json.dumps(json_raw.text[43:60:2])
    print(f"Answer: {varNew} Sean Higgins")
elif xVar =="3":
    json_raw = requests.get(URL)
    myDict = json_raw.headers
    x = myDict["MATC-HEADER"]
    print (f"Answer: {x}")
elif xVar =="4":
    json_raw = requests.get(URL)
    varNew = json.dumps(json_raw.text[453:462:])
    print(f"Answer: {varNew}")
elif xVar =="5":
    HOST = "172.31.29.253"
    PORT = 5150
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"secret")
        data = s.recv(1024)
    print(f"Answer: {data}")
else:
    print("Try again")

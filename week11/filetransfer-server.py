#!/usr/bin/env python3
import socket

# Empty quotes means listen on all available interfaces
LHOST = '127.0.0.1'
# Arbitrary non-privileged port to listen on             	
LPORT = 5000
RCV_DATA = "testfile.txt"         	

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while(1):
    	L_SOCK.listen(1)
    	L_CONN, addr = L_SOCK.accept()
    	print('Connected by', addr)
    	while 1:
            RCV_DATA = L_CONN.recv(1024)
            if not RCV_DATA: break
            print(f"The server received this data:{RCV_DATA}")
            # This line sends the data back to the client
            L_CONN.sendall(RCV_DATA)

    	L_CONN.close()


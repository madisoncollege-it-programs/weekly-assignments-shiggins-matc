#!/usr/bin/env python3
import socket

RHOST    = socket.gethostbyaddr('127.0.0.1') # The target IP address, retrieved by FQDN
RPORT    = 5000 # The target port as used by the server
SND_DATA = b"words"
RCV_DATA = ""


C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The connect() function handles the handshake 
# client -> server [SYN]
# client <- server [SYN,ACK]
# client -> server [ACK]
C_SOCK.connect((RHOST, RPORT))

# the send() function pushes your SND_DATA variable to the server.
# client -> server [PSH, ACK]
# client <- server [ACK]
C_SOCK.send(SND_DATA)

# The recv() function catches data returned (pushed) from the server and stores # it in the RCV_DATA variable.
# client <- server [PSH, ACK]
# client -> server [ACK]
RCV_DATA = C_SOCK.recv(1024)

# This will print out the data returned from the server
print(RCV_DATA.decode())

# close() initiates the socket shutdown sequence
# client -> server [FIN, ACK]
# client <- server [FIN, ACK]
# client -> server [ACK]
C_SOCK.close()

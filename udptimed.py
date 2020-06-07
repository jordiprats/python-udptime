import socket
import time
import sys

debug = True

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 1234)
print ('updtimed: UPD time listening on %s port %s' % server_address)
sock.bind(server_address)

while True:
    if debug:
        print ('udptimed: waiting to receive message')
    data, address = sock.recvfrom(4096)
    
    if debug:
        print ('udptimed: received %s bytes from %s' % (len(data), address))
        print (data)
    
    if data:
        decoded_str = data.decode("utf-8") 
        if decoded_str=='em sabria dir la data, si us plau?':
            response = str(int(time.time()))
            sent = sock.sendto(str.encode(response), address)
            if debug:
                print ('udptimed: sent %s bytes back to %s' % (sent, address))



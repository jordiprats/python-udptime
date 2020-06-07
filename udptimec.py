import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 1234)
message = 'em sabria dir la data, si us plau?'

debug = True

try:
    # Send data
    if debug:
        print('udptimec: sending "%s"' % message)
    sent = sock.sendto(str.encode(message), server_address)

    # Receive response
    if debug:
        print('idptimec: waiting to receive')
    data, server = sock.recvfrom(4096)
    if data:
        response = data.decode("utf-8")
        if debug:
            print('udptimec: received "%s"' % response)

finally:
    if debug:
        print('udptimec: closing socket')
    sock.close()

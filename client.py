#client

import socket
import sys
   
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data_to_sent = 'hello tcp socket'
try:
        sock.connect(('192.168.1.104', 80))

        sent = sock.send(data_to_sent)
        print(sock.recv(1024))
finally:
        sock.close()
        print('socket closed')
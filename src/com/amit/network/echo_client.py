'''
Created on 8 Aug. 2018

@author: Amit.Kumar1
'''
import socket
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

#server_address = './uds_socket'
#print >>sys.stderr, 'connecting to %s' % server_address
try:
    client_sock.connect((host, 8181))
    while True:
        msg = input()
        msg_to_send = msg.encode(encoding='ascii', errors='strict')
        client_sock.sendall(msg_to_send)
        amt_send = len(msg_to_send)
        amt_rcv = 0
        data = []
        while amt_rcv < amt_send:
            chunk = client_sock.recv(16)
            if chunk == b'':
                raise RuntimeError("Socket connection broken")
            amt_rcv += len(chunk)
            data.append(chunk)
        str_msg_rcv = b''.join(data).decode("ascii")
        print("Received %s" % str_msg_rcv)
except socket.error as msg:
    print(sys.stderr, msg)
finally:
    client_sock.close()
    

'''
Created on 30 Aug. 2018

@author: Amit.Kumar1
'''
import socket
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

try:
    client_sock.connect((host, 8181))
    while True:
        msg = input()
        print(msg)
        
        msg_to_send = msg.encode(encoding='ascii', errors='strict')
        if msg != "END":
            orig,end,hops = msg.split(',')
            print("%s\t%s\t%s" % (orig, end, hops))
        client_sock.sendall(msg_to_send)
        amt_send = len(msg_to_send)
        amt_rcv = 0
        data = []
        
        chunk = client_sock.recv(16)
        if chunk == b'':
            raise RuntimeError("Socket connection broken")
        str_msg_rcv = chunk.decode("ascii")
        print("Received %s" % str_msg_rcv)
        if str_msg_rcv == "END":
            break;
except socket.error as msg:
    print(sys.stderr, msg)
finally:
    client_sock.close()

'''
Created on 6 Mar. 2018

@author: Amit.Kumar1
'''

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9991

server_socket.bind((host, port))
server_socket.listen(1)

while True:
    client_socket, addr = server_socket.accept()
    print("Got a connection from: %s" % str(addr))
    
    data = client_socket.recv(1024)
    print(data)
    if len(data) > 2:
        file_name = data[2:].decode("utf-8")
        try:
            file_handle = open(file_name, "rb")
            buf = file_handle.read(1024)
            while buf:
                client_socket.send(buf)
                print('sent: ', repr(buf))
                buf = file_handle.read(1024)
        except IOError as ioe:
            print(str(ioe))
            
    client_socket.close()

'''
Created on 8 Aug. 2018

@author: Amit.Kumar1
'''
import socket
import sys
import os
import threading

class ClientThread(threading.Thread):
    def __init__(self, ip, port, sock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.cli_sock = sock
    
    def run(self):
        try:
            while True:
                data = self.cli_sock.recv(16)
                if data:
                    str_data = data.decode("ascii")
                    if str_data == 'END':
                        self.cli_sock.shutdown(1)
                        self.cli_sock.close()
                        break
                    else:
                        print("Received data %s" % str_data)
                        self.cli_sock.sendall(data)
                else:
                    pass
        finally:
            self.cli_sock.close()
            pass

def listen():
#server_address = './uds_socket'

#try:
#    os.unlink(server_address)
#except OSError:
#    if os.path.exists(server_address):
#        raise
    host = socket.gethostname()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, 8182))
    
    while True:
        server_socket.listen(5)
        (conn, (ip, port)) = server_socket.accept()
        newThread = ClientThread(ip, port, conn)
        newThread.start()

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass

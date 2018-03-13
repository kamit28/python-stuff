'''
Created on 7 Mar. 2018

@author: Amit.Kumar1
'''

#namp based port scanner - TCP scanner
import socket

client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

for port in range(9990, 9999):
    try:
        client_soc.connect((host, port))
        client_soc.close()
        print("Port " + str(port) + " is open")
    except Exception as e:
        print("Could not connect to port: " + str(port) + ": " + str(e))
        pass

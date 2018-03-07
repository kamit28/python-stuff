'''
Created on 6 Mar. 2018

@author: Amit.Kumar1
'''
import socket

nist_addr = ("time-a.nist.gov", 13)

time_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time_client.connect(nist_addr)

data = time_client.recv(128)
print(repr(data))

'''
Created on 6 Mar. 2018

@author: Amit.Kumar1
'''
import socket

client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9991

client_soc.connect((host, port))

msg = "c:/Users/Amit.Kumar1/java/8/streams/java8streams.rss"

client_soc.send(msg.encode(encoding='ascii', errors='strict'))

with open('c:/Users/Amit.Kumar1//Downloads/received_file.txt', 'wb') as f:
    while True:
        print('receiving data...')
        data = client_soc.recv(1024)
        if not data:
            break
        f.write(data)
f.close()
print('Succesfully received file')

client_soc.close()

'''
Created on 9 Aug. 2018

@author: Amit.Kumar1
'''
import sys
import socket

filename = "C:/Users/Amit.Kumar1/Documents/training.txt"
tree = {}

class BankNode:
    def __init__(self, start, end):
        self.parent = start
        self.name = end

## Use this function to write data to socket
#where connection is the socket object and message is string
def write_string_to_socket(connection, message):
    print("")

## Function to read data from socket
# where connection is the socket object
def read_string_from_socket(connection):
    try:
        data = connection.recv(128)
        if data:
            str_data = data.decode("ascii")
            if str_data == 'END':
                connection.shutdown(1)
                connection.close()
            else:
                print("Received data %s" % str_data)
                connection.sendall(data)
        else:
            pass
    finally:
        connection.close()
        pass


## This function is called only once before any client connection is accepted by the server.
## Read any global datasets or configurations here
def init_server():
    print("Reading training set")
    read_training_data(filename, tree)
    sys.stdout.flush()
    

def insert_node_in_tree(tree, start, end):
    node = BankNode(start, end)
    if tree.__contains__(start):
        tree[start].append(node)
    else:
        tree[start] = [node]


## This function is called every time a new connection is accepted by the server.
## Service the client here
def process_client_connection(connection):

    while True:
        # read message 
        message = read_string_from_socket(connection)

        print("Message received = ", message)

        # write message
        write_string_to_socket(connection, message)

        if message == "END":
            break

def read_training_data(filename, tree):
    try:
        file_handle = open(filename, "r")
        
        count = 0
        for line in file_handle:
            data = line.rstrip('\n')
            if count == 0:
                num_nodes = (int)(data)
                print(num_nodes)
                count += 1
            else:
                count += count
                (start,end) = data.split(",")
                insert_node_in_tree(tree, start, end)
                #print(tree, start, end)
    finally:
        file_handle.close()

def print(tree):
    for key in tree:
        node_list = tree.get(key)
        nodes_str = ''
        for item in node_list:
            nodes_str = nodes_str + ", " + item.name
        print(key + ": " + nodes_str)

if __name__ == '__main__':
    
    init_server()
    
    
    

        

    
        
        
        
        
        
        
        
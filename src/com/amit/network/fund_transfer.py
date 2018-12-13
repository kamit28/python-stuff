'''
Created on 29 Aug. 2018

@author: Amit.Kumar1
'''
import sys
import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, ip, port, sock):
        self.ip = ip
        self.port = port
        self.cli_sock = sock
        self.stop_request = threading.Event()
        threading.Thread.__init__(self)
    
    def run(self):
        self.stop_request.clear()
        while not self.stop_request.isSet():
            try:
                process_client_connection(self.cli_sock)
                self.stop_request.set()
                #sys.exit()
            except socket.error:
                pass
            finally:
                self.cli_sock.shutdown(socket.SHUT_WR)
                self.cli_sock.close()


    def join(self, timeout=None):
        self.stop_request.set()
        super(ClientThread, self).join(timeout)

def listen():
    host = socket.gethostname()
    port = 8181
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    threads = []
    
    while True:
        server_socket.listen(5)
        (conn, (ip, port)) = server_socket.accept()
        newThread = ClientThread(ip, port, conn)
        newThread.start()
        threads.append(newThread)

    for th in threads:
        th.join()


## Use this function to write data to socket
def write_string_to_socket(connection, message):
    connection.sendall(message.encode('utf-8'));

## Use this function to read data from socket
def read_string_from_socket(connection):
    data = connection.recv(1024)
    str_data = data.decode("ascii")
    return str_data
    

## All global declarations go here
adj_mat = []
num_nodes = 0

## This function is called only once before any client connection is accepted by the server.
## Read any global datasets or configurations here
def init_server():
    global num_nodes
    global adj_mat
    print("Reading training set")
    sys.stdout.flush()
    counter = 0
    try:
        file_handle = open("C:/Users/Amit.Kumar1/Desktop/network_config.txt", "r")
        
        for line in file_handle:
            if counter == 0:
                num_nodes = int(line)
                adj_mat = [[0 for x in range(num_nodes+1)] for y in range(num_nodes+1)]
            else:
                orig,end = line.split(',')
                adj_mat[int(orig)][int(end)] = 1;
                adj_mat[int(end)][int(orig)] = 1;
            counter += 1
    finally:
        file_handle.close()
        
    print("Finished reading network config data")
    for i in range (1, num_nodes+1):
        for j in range (1, num_nodes+1):
            print("%d\t" % adj_mat[i][j], end='', flush=True)
        print("")
    ## Open server socket and start listening
    listen()
    

def check_transfer_possibility(node, target, hops):
    global num_nodes
    global adj_mat
    visited = [False] * (num_nodes+1)
    queue = []
    queue.append(node)
    visited[node] = True
    while queue and hops > 0:
        v = queue.pop(0)
        hops -= 1
        if v == target:
            return "YES"
        for i in range(1, num_nodes+1):
            if adj_mat[v][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
    return "NO"
    
   # if hops == 0:
   #     return "No"
   # elif node == target:
    #    return "Yes"
   # else:
   #     for i in (1, num_nodes):
   #         if adj_mat[node][i] == 1 and visited[i] == False:
   #             return check_transfer_possibility(i, target, hops-1)

## This function is called every time a new connection is accepted by the server.
## Service the client here
def process_client_connection(connection):
    global num_nodes
    while True:
        # read message 
        message = read_string_from_socket(connection)
        
        print ("Message received = ", message)
        if message == "END":
            write_string_to_socket(connection, message)
            break
        else:
            orig,end,hops = message.split(',')
            #print("%d\t%d\t%d" % (int(orig), int(end), int(hops)))
            message = check_transfer_possibility(int(orig), int(end), int(hops))
            # write message
            write_string_to_socket(connection, message)


if __name__ == '__main__':
    init_server()

    
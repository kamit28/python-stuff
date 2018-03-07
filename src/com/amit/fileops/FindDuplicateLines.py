'''
Created on 22 Feb. 2018

@author: Amit.Kumar1
'''
# import hashlib

file_name = input("Enter file name with full path: ")
already_visited = {}
try:
    file_handle = open(file_name, "r")

    for line in file_handle:
        # line_hash = hashlib.md5(line.encode())
        if(already_visited.__contains__(line)):
            count = already_visited.get(line)
            already_visited[line] = count + 1
        else:
            already_visited[line] = 1
finally:
    file_handle.close()

for key, val in already_visited.items():
    if val > 1:
        print("Duplicate line: ", key.rstrip(), " appeared: ", val, " times")

    

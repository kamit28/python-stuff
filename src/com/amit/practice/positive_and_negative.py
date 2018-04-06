'''
Created on 21 Mar. 2018

@author: Amit

Program to arrange a negative number after each positive number
'''
import sys

def find_next_index(arr, pos, direction=1):
    if pos >= len(arr):
        return None
    while pos < len(arr):
        if direction == 1 and arr[pos] > 0:
            return pos
        elif direction == 1 and arr[pos] > 0:
            return pos
        else:
            pos += 1
    return None

inputs = []
val = int(sys.stdin.readline())
for i in range(0, val):
    num_elem = int(sys.stdin.readline())
    elems = list(map(int, sys.stdin.readline().split()))
    inputs.append(elems)

for elems in inputs:
    for index in range(0, len(elems) - 1):
        next_index = 0
        swap = False
        if index % 2 == 0 and elems[index] < 0:
            next_index = find_next_index(elems, index+1, 1)
            swap = True
        elif index % 2 == 1 and elems[index] > 0:
            next_index = find_next_index(elems, index+1, -1)
            swap = True
        if next_index is None:
            break;
        elif swap:
            elems[index], elems[next_index] = elems[next_index], elems[index]
            
    print(*elems, sep=' ')

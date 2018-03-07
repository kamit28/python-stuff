'''
Created on 19 Feb. 2018

@author: Amit.Kumar1
'''


class MyStack:
    
    def __init__(self, max_size):
        self.arr = []
        self.top = -1
        self.max_size = max_size
        
    def push(self, val):
        self.arr.append(val)
        self.top += 1
        return
    
    def pop(self):
        val = self.arr[self.top]
        self.top -= 1
        return val
    
    def empty(self):
        return self.top == -1
    
    def full(self):
        return self.top + 1 == self.max_size

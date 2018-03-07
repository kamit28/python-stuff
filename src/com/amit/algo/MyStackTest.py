'''
Created on 19 Feb. 2018

@author: Amit.Kumar1
'''

from MyStack import MyStack

my_stack = MyStack(10)
val = 1
while (my_stack.full() == False):
    my_stack.push(val)
    val += 1
while (my_stack.empty() == False):
    print(my_stack.pop())


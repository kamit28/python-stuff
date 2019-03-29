'''
Created on 19 Mar. 2018

@author: Amit.Kumar1
'''
def receiver():
    while True:
        item = yield
        print('Got', item)

recv = receiver()
next(recv)
recv.send('Hello')
recv.send('World')

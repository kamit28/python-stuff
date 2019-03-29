'''
Created on 8 Mar. 2018

@author: Amit.Kumar1
'''
import threading
import time

def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" %(thread_name, time.ctime(time.time())))

our_threads = []
try:
    t1 = threading.Thread(name= 'thread-1', target=print_time, args=('thread-1', 5))
    t2 = threading.Thread(name= 'thread-2', target=print_time, args=('thread-2', 1))
    our_threads.append(t1)
    our_threads.append(t2)
    t1.start()
    t2.start()

except:
    print("Exception occurred")

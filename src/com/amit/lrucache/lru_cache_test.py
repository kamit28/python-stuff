'''
Created on 14 Mar. 2018

@author: Amit.Kumar1
'''
from com.amit.lrucache.lrucache import LruCache

mycache = LruCache(10)

mycache.put('A1')
mycache.put('A2')
mycache.put('A3')
mycache.put('A4')
mycache.put('A5')
mycache.put('A6')
mycache.put('A7')
mycache.put('A8')
mycache.put('A9')
mycache.put('A10')

# should return A1
print(mycache.get('A1'))

#should return None
print(mycache.get('1A'))

mycache.put('A11')

#this should return A1
print(mycache.get('A1'))

#this should return A2
print(mycache.get('A2'))

#this should return A11
print(mycache.get('A11'))
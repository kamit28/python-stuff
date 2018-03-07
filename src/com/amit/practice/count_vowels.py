'''
Created on 2 Mar. 2018

@author: Amit.Kumar1
'''

from functools import reduce

input_str = input("Enter a String: ")
'''
for v in filter(lambda x : x in ('a', 'e', 'i', 'o' , 'u'), input_str):
    if v in frequency:
        frequency[v] += 1
    else:
        frequency[v] = 1
print(str(frequency))
'''
frequency = {}
result = dict(map(lambda k : (k, frequency[k] + 1) if k in frequency else (k, 1), filter(lambda x : x in ('a', 'e', 'i', 'o' , 'u'), input_str)))
print(str(result))

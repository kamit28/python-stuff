'''
Created on 19 Feb. 2018

@author: Amit.Kumar1
'''

memo = [0, 1]


def firstNFibonacci(n):
    if n < 2:
        return memo[n - 1]
    else:
        temp = firstNFibonacci(n - 2) + firstNFibonacci(n - 1)
        memo.append(temp)
        return temp

    
n = 5
val = firstNFibonacci(n)
print(val)

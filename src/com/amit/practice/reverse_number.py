'''
Created on 23 Feb. 2018

@author: Amit.Kumar1
'''

num = int(input("Enter a number: "))
rev = 0
while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

print(rev)

'''
Created on 14 Jan. 2019

@author: Amit.Kumar1
'''

def gcd_xy(x, y):
    
    if x == y:
        return x
    if x == 0:
        return y
    if y == 0:
        return x
    
    if x & 1 == 0:
        if y & 1 == 0:
            return gcd_xy(x >> 1, y >> 1) << 1
        else:
            return gcd_xy(x >> 1, y)
    if y & 1 == 0:
        return gcd_xy(x, y >> 1)
    if x > y and y & 1 != 0:
        return gcd_xy((x - y) >> 1, y)
    return gcd_xy((y - x) >> 1, x)

def gcd(*args):
    if len(args) == 1:
        return args[0]
    elif len(args) >= 2:
        gcd = gcd_xy(args[0], args[1])
        for i in range(2, len(args)):
            gcd = gcd_xy(gcd, args[i])
        return gcd

print(gcd(24, 32, 48))
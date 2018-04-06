'''
@author: Amit

Program for LCM of n numbers
'''

from com.amit.practice.calc_gcd import gcd_xy


def lcm_xy(x, y):
    return (x * y // gcd_xy(x, y))


def lcm(*args):
    if len(args) == 1:
        return args[0]
    elif len(args) >= 2:
        lcm = lcm_xy(args[0], args[1])
        for i in range(2, len(args)):
            lcm = lcm_xy(lcm, args[i])
        return lcm


print(lcm(12, 4, 8))

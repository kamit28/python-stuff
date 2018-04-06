''' Program for GCD of n numbers '''

def gcd_xy(x, y):
    while y:
        x, y = y, x % y
    return x


def gcd(*args):
    if len(args) == 1:
        return args[0]
    elif len(args) >= 2:
        gcd = gcd_xy(args[0], args[1])
        for i in range(2, len(args)):
            gcd = gcd_xy(gcd, args[i])
        return gcd

#print(gcd(24, 32, 48))

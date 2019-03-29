'''
Created on 7 Jan. 2019

@author: Amit.Kumar1
'''
class Unary:
    def __init__(self, val):
        self.y = val
    
    def __neg__(self):
        return -self.y
    
    def __pos__(self):
        return self.y

if __name__ == "__main__":
    obj1 = Unary(2)
    print(-obj1)
    print(+obj1)
    print(~obj1.y)

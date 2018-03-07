'''
Created on 28 Feb. 2018

@author: Amit.Kumar1
'''
from com.amit.algo.dl_list import dl_list

my_list = dl_list()
my_list.add_front(10)
my_list.add_last(20)
my_list.add_last(30)
my_list.add_last(40)
my_list.add_last(50)
my_list.add_front(0)
the_4th = my_list.get(3);
print(the_4th)
my_list.add(25, 3)
my_list.add(55, 7)
my_list.print_list()
my_list.remove_front()
my_list.remove_last()
my_list.add_front(100)
my_list.add_last(200)
my_list.print_list()
print(my_list.get_first())
print(my_list.get_last())
print(my_list.get(2))
print(my_list.get(0))
print(my_list.get(my_list.size - 1))
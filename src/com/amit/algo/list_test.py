#!/usr/bin/python

from linked_list import linked_list
from linked_list import Node

list = linked_list()
list.add(1)
list.add(2)
list.add(3)
list.print_list()
list.add_front(4)
second_node = list.get_node(2)
list.add_after(second_node, 5)
list.print_list()
list.del_first()
list.del_last()
list.print_list()


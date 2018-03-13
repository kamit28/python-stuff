'''
Node class for linked list nodes
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class for linked list
'''
class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        temp = self.head
        while (temp):
            print temp.data
            temp = temp.next

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node
        self.size += 1
        return True;

    def get_node(self, index):
        temp = self.head
        pos = 0
        while (temp.next and pos < index):
            temp = temp.next
            pos += 1
        if temp:
            return temp
        else:
            return None

    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return True

    def add_after(self, the_node, data):
        if the_node is None:
            print "The given node must not be null"
            return False
        new_node = Node(data)
        new_node.next = the_node.next
        the_node.next = new_node
        self.size += 1
        return True

    def del_node(self, the_node):
        if the_node is None:
            print "The given node must not be null"
            return False
        
        temp = self.head
        while temp.next != the_node:
            temp = temp.next
        temp.next = the_node.next
        the_node.next = None
        self.size -= 1
        return True

    def del_first(self):
        if self.head is None:
            print "list is empty"
            return False

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        return True

    def del_last(self):
        if self.head is None:
            print "list is empty"
            return False

        temp = self.head
        temp_prev = self.head
        while temp.next != None:
            temp_prev = temp
            temp = temp.next

        temp_prev.next = None
        temp = None
        self.size -= 1
        return True


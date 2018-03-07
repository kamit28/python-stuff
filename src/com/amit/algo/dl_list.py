'''
Created on 26 Feb. 2018

@author: Amit.Kumar1
'''


class dl_node:
    'node class for a doubly-linked list'

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
    def __str__(self):
        return str(self.__dict__)
    
    def __eq__(self, other):
        return isinstance(self.__class__, other) and self.__dict__ == other.__dict__
    

class dl_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get_node(self, index):
        if self.size == 0:
            raise Exception("List is empty")
        if self.size - 1 < index:
            raise Exception("Index out of range: " + str(index))
        temp = None
        if index < (self.size >> 1):
            temp = self.head
            for i in range(0, index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.size - 1, index, -1):
                temp = temp.prev
        return temp
    
    def add_front(self, data):
        new_node = dl_node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return True
    
    def add_last(self, data):
        new_node = dl_node(data)
        
        if self.tail is None:
            self.add_front(data)
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return True
    
    def add_after(self, prev_node, data):
        new_node = dl_node(data)
        
        new_node.next = prev_node.next
        new_node.prev = prev_node
        new_node.next.prev = new_node
        prev_node.next = new_node
        self.size += 1
        return True
    
    def add_before(self, next_node, data):
        new_node = dl_node(data)
        
        new_node.next = next_node
        new_node.prev = next_node.prev
        next_node.prev.next = new_node
        next_node.prev = new_node
        self.size += 1
        return True
    
    def add(self, data, index):
        if index < 0 and index >= self.size:
            raise ValueError("Index out of range")
        if index == self.size:
            self.add_last(data)
            return True
        self.add_before(self.get_node(index), data)
        return True
    
    def remove_front(self):
        if self.head is None:
            print("List is empty!!")
            return False
        temp_node = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp_node.next;
            temp_node.next = None
            self.head.prev = None
        self.size -= 1
        temp_node = None
        return True
    
    def remove_last(self):
        if self.size == 0:
            print("List is empty!!")
            return False
        temp_node = self.tail
        if self.size == 1:
            self.remove_front()
        else:
            self.tail = temp_node.prev;
            temp_node.prev = None
            self.tail.next = None
        self.size -= 1
        temp_node = None
        return True
    
    '''
    Removes a specified node, if its exists.
    The list remains unchanged if the node is not present.
    '''

    def remove_node(self, a_node):
        if a_node is not None:
            if self.size == 1:
                self.remove_front()
            else:
                a_node.prev.next = a_node.next
                a_node.next.prev = a_node.prev
                a_node = None
                self.size -= 1
            return True
        else:
            print("Node can't be null")
            return False
    
    '''
    Removes the first occurrence of the of the specified element, if it is present.
    The list remains unchanged if the element is not present.
    '''

    def remove(self, data):
        temp_node = self.head
        if data is None:
            while temp_node is not None:
                if temp_node.data is None:
                    self.remove_node(temp_node)
                    return True
                temp_node = temp_node.next
        else:
            while temp_node is not None:
                if temp_node.data == data:
                    self.remove_node(temp_node)
                    return True
                temp_node = temp_node.next
    
    def get_first(self):
        if self.size == 0:
            raise Exception("List is empty")
        return self.head.data
    
    def get_last(self):
        if self.size == 0:
            raise Exception("List is empty")
        return self.tail.data
    
    def get(self, index):
        if self.size == 0:
            raise Exception("List is empty")
        if self.size - 1 < index:
            raise Exception("Index out of range: " + str(index))
        temp = self.get_node(index)
        return temp.data
    
    def print_list(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.data)
            result += "\t"
            temp = temp.next
        print(result)
    

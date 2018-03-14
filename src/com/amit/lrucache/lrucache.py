'''
@author: Amit
'''
from com.amit.algo.dl_list import dl_list
import threading

class LruCache():
    def __init__(self, size):
        self.max_size = size;
        self.lru_list = dl_list()
        self.data = {}
        self.size = 0
        self.mutex = threading.RLock()
        self.not_empty = threading.Condition(self.mutex)
    
    def is_full(self):
        with self.mutex:
            return self.size == self.max_size
    
    def put(self, obj):
        with self.mutex:
            if self.is_full():
                self.evict()
            obj_hash = hash(obj)
            self.data[obj_hash] = obj
            self.size += 1
            self.lru_list.add_last(obj_hash)
            if self.size == 1:
                self.not_empty.notifyAll()
    
    def evict(self):
        with self.mutex:
            obj_hash = self.lru_list.get_first()
            del self.data[obj_hash]
            self.lru_list.remove_front()
            self.size -= 1
    
    def get(self, obj):
        with self.not_empty:
            if self.contains(obj):
                with self.mutex:
                    obj_hash = hash(obj)
                    self.lru_list.remove_front()
                    self.lru_list.add_last(obj_hash)
                    return self.data.get(obj_hash)
            return None
    
    def contains(self, obj):
        with self.mutex:
            return hash(obj) in self.data

class node(object): # double linked list node
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity # Cache capacity
        self.cache = dict()
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.mark_most_recent(self.cache[key])
            return self.cache[key].val
            print(self.tail.val)
            print("\n")
        else:
            return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.cache: # key already present
            self.cache[key].val = value
            self.mark_most_recent(self.cache[key])
        else: # not present
            new_node = node(key, value)
            self.cache[key] = new_node
            self.mark_most_recent(self.cache[key])
        if len(self.cache) > self.capacity: # cache overflow, remove least recent element
            self.remove_tail_node()
        print(self.tail.val)
        print("\n")
 
    def mark_most_recent(self, node):
        
        if node == self.head:
            return
        if self.tail == node:
            self.tail = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
            
    
    def remove_tail_node(self):
        del self.cache[self.tail.key]
        self.tail = self.tail.next

obj = LRUCache(3)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.put(4,4)
obj.get(4)
obj.get(3)
obj.get(2)
obj.get(1)
obj.put(5,5)
obj.get(1)
obj.get(2)
obj.get(3)

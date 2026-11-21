
class Node:
    def __init__(self,key,value):
        self.val = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memory = {}
        
        # To avoid handling None values, both tail and head ar dummy nodes
        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        # Linked them so that there arent null pointers
        self.head.prev= self.tail
        self.tail.next = self.head
                
    def insert(self,node:Node):        
        # Insert a new node at the end of the LRU DLL
        prev = self.head.prev
        
        prev.next = node
        node.next = self.head
        node.prev = prev
        self.head.prev = node        
                
        
    def remove(self, node:Node):
        prev,next = node.prev,node.next
        
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.memory:
            # Update LRU
            node = self.memory[key]            
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Validate if that key already exists
        
        if key in self.memory:
            # Key already exists
            
            # Update its value
            node = self.memory[key]
            node.val = value            
            # Update LRU
            self.remove(node)
            self.insert(node)            
            return
        
        if len(self.memory) == self.capacity:
            # Remove tail from LRU and memory and insert new record
            nodeToRemove = self.tail.next            
            self.remove(nodeToRemove)
            del self.memory[nodeToRemove.key]
            
            node = Node(key,value)
            self.insert(node)
            self.memory[key] = node
        else:
            # within capacity, add new node            
            node = Node(key,value)
            self.memory[key] = node
            
            # Insert node on LRU
            self.insert(node)
        


lRUCache = LRUCache(2);
print(lRUCache.put(1, 1)); # cache is {1=1}
print(lRUCache.put(2, 2)); # cache is {1=1, 2=2}
print(lRUCache.get(1));    # return 1
print(lRUCache.put(3, 3)); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2));    # returns -1 (not found)
print(lRUCache.put(4, 4)); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1));    # return -1 (not found)
print(lRUCache.get(3));    # return 3
print(lRUCache.get(4));    # return 4
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Dictionary to handle the key value pairs
        self.memory = {}
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.memory:
            idxOfKey = self.lru.index(key)
            self.lru.pop(idxOfKey)
            self.lru.append(key) ## Append at the end
            return self.memory[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.memory:
            # Replace content
            self.memory[key] = value
            idxOfKey = self.lru.index(key)
            self.lru.pop(idxOfKey)
            self.lru.append(key) ## Append at the end
                
        elif len(self.memory) == self.capacity:            
            # Memory at full capacity, this insert will remove data            
            # Remove data            
            # Determina which key
            keyToRemove = self.lru[0]                   
            del self.memory[keyToRemove]            
            # Remove element form lru
            self.lru.pop(0)
            
            # Insert new data
            self.memory[key] = value
            self.lru.append(key)                        
        else:
            self.memory[key] = value
            self.lru.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache =LRUCache(2);
print(lRUCache.put(1, 1)); # cache is {1=1}
print(lRUCache.put(2, 2)); # cache is {1=1, 2=2}
print(lRUCache.get(1));    # return 1
print(lRUCache.put(3, 3)); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2));    # returns -1 (not found)
print(lRUCache.put(4, 4)); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1));    # return -1 (not found)
print(lRUCache.get(3));    # return 3
print(lRUCache.get(4));    # return 4
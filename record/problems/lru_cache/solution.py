class Node:
    def __init__(self, key=-1, val=-1):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.defaultdict(Node)
        self.lru, self.mru = Node(), Node() 
        self.lru.next, self.mru.prev = self.mru, self.lru
    
    def delete(self, node):
        prev_node = node.prev 
        next_node = node.next 
        prev_node.next = next_node 
        next_node.prev = prev_node
        
    
    def insert(self, node):
        prev_node = self.mru.prev
        prev_node.next = node 
        self.mru.prev = node 
        node.prev = prev_node 
        node.next = self.mru
        
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node = self.cache[key]
            self.delete(node)
        self.cache[key] = Node(key=key, val=value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru_node = self.lru.next 
            self.delete(lru_node)
            del self.cache[lru_node.key]
        
         
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
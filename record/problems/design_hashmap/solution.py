class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.size = 2069
        # dummyHead
        self.table = [ ListNode(-1,-1) for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        hashKey = key % self.size 
        dummyHead = self.table[hashKey]
        node = dummyHead
        
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return 
            node = node.next 
        node.next = ListNode(key,value)
        
    def get(self, key: int) -> int:
        hashKey = key % self.size 
        dummyHead = self.table[hashKey]
        node = dummyHead
        
        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        hashKey = key % self.size 
        dummyHead = self.table[hashKey]
        node = dummyHead
        prev = dummyHead 
        
        while node.next:
            if node.next.key == key:
                prev.next = prev.next.next 
                return 
            node = node.next 
            prev = prev.next 
            
        
       
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = Node(-1,-1)
        
    def add(self, key, value):
        newnode = Node(key, value)
        
        # 1) 如果linkedlist 里面没有(key,val) , add node to the tail
        # 2) 如果有, 就改变value
        cur = self.root 
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next 
        cur.next = newnode
    
    def get(self, key):
        cur = self.root 
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1
    
    def remove(self, key):
        cur = self.root 
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next 
                return          
            cur = cur.next
            
class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.bucket = [LinkedList() for _ in range(self.size)]  

    def put(self, key: int, value: int) -> None:
        hashkey = key % self.size  
        curLinkedlist = self.bucket[hashkey]
        curLinkedlist.add(key,value)
        
    def get(self, key: int) -> int:
        hashkey = key % self.size
        curLinkedlist = self.bucket[hashkey]
        return curLinkedlist.get(key)
        
    def remove(self, key: int) -> None:
        hashkey = key % self.size 
        curLinkedlist = self.bucket[hashkey]
        curLinkedlist.remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
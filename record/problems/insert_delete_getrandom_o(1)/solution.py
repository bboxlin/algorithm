import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.lookup = {}

    def insert(self, val: int) -> bool:
        if val in self.lookup.keys(): return False 
        self.lookup[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup.keys(): return False
        idx = self.lookup[val]
        
        # update arr
        lastval = self.arr[-1]
        self.arr[idx] = lastval
        self.arr.pop() 
        
        # update lookup
        self.lookup[lastval] = idx
        del self.lookup[val]
         
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
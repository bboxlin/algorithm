class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    '''
    When we get certain cache, its priority level being most recent
    By defacult of ordered dictionary, we have to del the item and add the item again
    so it stay at last index
    '''
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return self.cache[key]
        else:
            return -1

    '''
    When we put the new cache item, its priority should also be most recent
    two cases:
        1. when next item will overflow the capacity ("in which means capacity == length of cache and upcoming item not part of cache")
                : use iterator to get the first item and delete it
                : add the new item in
        2. otherwise,
                if new key exist, we delete it and re-add to make its priority most recent.
    '''
    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            first_key = next(iter(self.cache))
            del self.cache[first_key]
            self.cache[key] = value
        else:
            if key in self.cache:
                del self.cache[key]
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
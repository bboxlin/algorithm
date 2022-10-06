class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        lst = self.map[key]
        l, r = 0, len(lst)-1
        
        # binary search with closest to the right but not greater than timestamp
        ans = ""
        while l <= r:
            mid = (l+r) // 2
            if lst[mid][0] <= timestamp:
                ans = lst[mid][1]
                l = mid+1
            else:
                r = mid-1 
        return ans
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
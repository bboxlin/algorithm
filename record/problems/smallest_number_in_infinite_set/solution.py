class SmallestInfiniteSet:

    def __init__(self):
        self.pastMinSet = set()
        self.pastMinHeap = []
        self.min = 1

    def popSmallest(self) -> int:
        if self.pastMinHeap:
            res = heapq.heappop(self.pastMinHeap)
            self.pastMinSet.remove(res)
            return res 
        res = self.min
        self.min += 1 
        return res

    def addBack(self, num: int) -> None:
        if num < self.min:
            if num not in self.pastMinSet:
                heapq.heappush(self.pastMinHeap, num)
                self.pastMinSet.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
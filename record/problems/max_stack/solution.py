
class MaxStack:

    def __init__(self):
        self.maxheap = []
        self.remove = set()
        self.stack = []
        self.idx = 0
      
    def push(self, x: int) -> None:
        # when there is a tie to x, we want the largest idx one (most current)
        heapq.heappush(self.maxheap, (-x, self.idx))
        self.stack.append((x, self.idx))
        self.idx -= 1

    def pop(self) -> int:
        # clean up the removes first
        while self.stack and self.stack[-1][1] in self.remove:
            self.stack.pop()
        val, i = self.stack.pop()
        self.remove.add(i)
        return val
        
    def top(self) -> int:
        # clean up the removes first
        while self.stack and self.stack[-1][1] in self.remove:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.maxheap and self.maxheap[0][1] in self.remove:
            heapq.heappop(self.maxheap)
        return -self.maxheap[0][0]
    
    def popMax(self) -> int:
        while self.maxheap and self.maxheap[0][1] in self.remove:
            heapq.heappop(self.maxheap)
        val, i = heapq.heappop(self.maxheap)
        self.remove.add(i)
        return -val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
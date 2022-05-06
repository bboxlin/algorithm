import collections
class MyStack:

    def __init__(self):
        self.q = collections.deque()
        self.topVal = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.topVal = x

    def pop(self) -> int:
        print(self.q)
        for i in range(len(self.q) - 1):
            self.topVal = self.q.popleft()
            self.q.append(self.topVal)
        return self.q.popleft()
    
    def top(self) -> int:
        return self.topVal

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
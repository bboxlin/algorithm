class Node:
    def __init__(self, val, minVal, nxt):
        self.minVal = minVal
        self.val = val
        self.nxt = nxt

class MinStack:
    def __init__(self):
        self.head = None 

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, val, None)
        else:
            nxtNode = Node(val, min(self.head.minVal, val), self.head)
            self.head = nxtNode      

    def pop(self) -> None:
        self.head = self.head.nxt

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.minVal

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# In Python, we have to make do with the OrderedDict class. We can use it as a Set by setting
# the values to None.

from collections import OrderedDict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self._queue = OrderedDict()
        self.seen = set()
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        if self._queue:
            return next(iter(self._queue))
        return -1
        
    def add(self, value: int) -> None:
        if value in self.seen:
            self._queue.pop(value, -1)
        else:
            self.seen.add(value)
            self._queue[value] = True

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
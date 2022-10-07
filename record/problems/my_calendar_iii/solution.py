from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.map = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.map[start] = self.map.get(start,0) + 1
        self.map[end] = self.map.get(end,0) - 1
        laps = 0
        ans = 0
        for v in self.map.values():
            laps += v
            ans = max(ans, laps)
        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
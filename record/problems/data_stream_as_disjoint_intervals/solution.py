class SummaryRanges:

    def __init__(self):
        self.nums = []
        self.seen = set()

    def addNum(self, value: int) -> None:
        if value in self.seen: return
        self.seen.add(value)
        self.nums.append(value)
        self.nums.sort()

    def getIntervals(self) -> List[List[int]]:
        if len(self.nums) == 0: 
            return [[0,0]]
        res = []
        i = 0 
        while i < len(self.nums):
            start = self.nums[i]
            end = self.nums[i]
            j = i + 1 
            while j < len(self.nums) and self.nums[j] == self.nums[j-1] + 1:
                end = self.nums[j]
                j += 1
            res.append([start,end])
            i = j
        return res
            



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
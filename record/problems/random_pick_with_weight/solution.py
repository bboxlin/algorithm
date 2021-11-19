class Solution:

    def __init__(self, w: List[int]):
        self. presum = []
        cursum = 0
        for n in w:
            cursum += n
            self.presum.append(cursum)
        self.total = cursum
        
    def pickIndex(self) -> int:
        ran = self.total * random.random()
        l,r = 0, len(self.presum)
        while l < r :
            mid = l + (r-l)//2
            if ran > self.presum[mid]:
                l = mid + 1
            else:
                r = mid
        return l
                
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
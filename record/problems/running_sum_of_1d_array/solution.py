class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        cursum = 0
        for i, n in enumerate(nums):
            cursum += n 
            res[i] = cursum
        return res
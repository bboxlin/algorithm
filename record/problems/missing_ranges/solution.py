class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if len(nums) == 0: 
            return [[lower, upper]]
        if nums[0] - lower >= 1:
            res.append([lower, nums[0]-1])
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                high = nums[i] - 1
                low  = nums[i-1] + 1
                res.append([low, high])
        if upper - nums[-1] >= 1:
            res.append([nums[-1]+1, upper]) 
        return res
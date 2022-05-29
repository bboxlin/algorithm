class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        i = 0
        while i < len(nums):
            j = i 
            while j < len(nums) and nums[j] == 1:
                j += 1
            windowSize = j - i
            maxx = max(windowSize, maxx)
            i = i + 1 if j == i else j
        return maxx
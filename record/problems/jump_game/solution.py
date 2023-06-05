class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0 
        n = len(nums)
        for i, v in enumerate(nums):
            if i > maxreach:
                return False
            maxreach = max(maxreach, i + v)
        return maxreach >= n - 1

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total = 0 
        n = len(nums) 
        minsize = inf
        l = 0 
        for r in range(n):
            total += nums[r]
            while total >= target:
                minsize = min(minsize, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if minsize == inf else minsize
        
         
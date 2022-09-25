class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        maxnum = max(nums)
        l = 0
        while l < len(nums):
            if nums[l] != maxnum: 
                l += 1
                continue 
            r = l
            while r < len(nums) and nums[r] == maxnum:
                r += 1
            ans = max(ans, r-l)
            l = r
        return ans
            
            
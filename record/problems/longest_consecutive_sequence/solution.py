class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums: return 0
#         container = set(nums)
#         maxlen = 0
#         for n in nums:
#             curlen = 1
#             # starting number
#             if n - 1 not in container:
#                 nxt = n + 1
#                 while nxt in container:
#                     nxt += 1
#                     curlen += 1
#             maxlen = max(curlen, maxlen)
#         return maxlen
    
        nums = sorted(list(set(nums)))
        maxlen = 0
        l = 0
        while l < len(nums):
            r = l + 1 
            curnum = nums[l]
            while r < len(nums) and nums[r] == curnum + 1:
                curnum = nums[r]
                r += 1
            maxlen = max(maxlen, r-l)
            l = r 
        return maxlen
            
            
                    
                    
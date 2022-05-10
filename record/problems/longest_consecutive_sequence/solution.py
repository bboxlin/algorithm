class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        container = set(nums)
        maxlen = 0
        for n in nums:
            curlen = 1
            # starting number
            if n - 1 not in container:
                nxt = n + 1
                while nxt in container:
                    nxt += 1
                    curlen += 1
            maxlen = max(curlen, maxlen)
        return maxlen
            
                    
                    
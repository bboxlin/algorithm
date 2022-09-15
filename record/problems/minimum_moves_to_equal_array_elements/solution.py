class Solution:
    
 
        
    def minMoves(self, nums: List[int]) -> int:
        minval = min(nums)
        ans = 0
        for num in nums:
            ans += num - minval
        return ans
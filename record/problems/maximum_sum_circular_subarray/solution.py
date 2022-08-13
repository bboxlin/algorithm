class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n = len(nums)
        maxdp = [0] * n
        mindp = [0] * n
        total = 0
        for i in range(n):
            if i == 0: 
                maxdp[0] = nums[0]
                mindp[0] = nums[0]
            else:
                maxdp[i] = max(nums[i], maxdp[i-1] + nums[i]) 
                mindp[i] = min(nums[i], mindp[i-1] + nums[i]) 
            total += nums[i]
        
        
        maxsub = max(maxdp)
        minsub = min(mindp)
        if minsub >= total: return maxsub
        return max(maxsub, total - minsub)  
    
 
 
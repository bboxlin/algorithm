class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
 
        lookup = defaultdict(int)
        for val in nums:
            lookup[val] += val 
        
         
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp = [0]*n
        
        
        for i in range(n):
            if i == 0: dp[i] = lookup[nums[i]]
            elif i == 1: dp[i] = max(dp[i-1], lookup[nums[i]]) if nums[i] == nums[i-1] + 1 else dp[i-1] + lookup[nums[i]] 
            elif nums[i] == nums[i-1] + 1:
                dp[i] = max( dp[i-1],  lookup[nums[i]] + dp[i-2] ) 
            else:
                dp[i] = dp[i-1] + lookup[nums[i]] 
        print(dp)
        return dp[n-1]
        
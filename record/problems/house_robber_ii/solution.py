class Solution:
    def rob(self, nums: List[int]) -> int: 
        def rob_amount(arr):
            n = len(arr)
            dp = n*[0]
            for i in range(n):
                if i == 0: dp[i] = arr[i]
                elif i == 1: dp[i] = max(dp[i-1], arr[i])
                else: dp[i] = max(dp[i-1], dp[i-2] + arr[i]) 
            return dp[n-1]
        
        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums)
        return max( rob_amount(nums[1:]), rob_amount(nums[:-1]) )
    
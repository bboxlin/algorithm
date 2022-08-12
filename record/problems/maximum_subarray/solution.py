class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            if i == 0: dp[0] = nums[0]
            else:
                dp[i] = max(nums[i], dp[i-1] + nums[i]) 
        return max(dp)
    
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        for i in range(n):
            if i == 0: dp[i] = 0
            maxnxt = min(i + nums[i], n-1)
            for j in range(i+1, maxnxt+1):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n-1]
                
            
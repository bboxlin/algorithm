class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            if i == 0: dp[i] = nums[i]
            else:
                # dp[i] stored the max reachable index
                dp[i] = max(i + nums[i], dp[i-1]) if dp[i-1] >= i else 0
        return max(dp) >= n-1
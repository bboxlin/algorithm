class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        for i in range(1,n+1):
            y = i & (i-1)
            dp[i] = dp[y] + 1
        return dp
             
        
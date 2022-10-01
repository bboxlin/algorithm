class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n+1):
            cur, prev = s[i-1], s[i-2]
            # 
            if '1' <= cur <= '9':
                dp[i] += dp[i-1] 
            if i > 1 and (prev == '1' or prev  == '2' and cur in '0123456'):   
                dp[i] += dp[i-2]
        return dp[n]
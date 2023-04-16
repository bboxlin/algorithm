class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        I = len(words[0])
        J = len(target)
        mod = 10**9 + 7 
        cnt = [[0]*26 for _ in range(I)]
        for word in words:
            for i, c in enumerate(word):
                cnt[i][ord(c) - ord('a')] += 1
        dp = [ [0]*J for _ in range(I) ]
        # dp[i][j] indicates num way to form target[..j] using word item[..i]
        # base case
        dp[0][0] = cnt[0][ord(target[0]) - ord('a')]
        for i in range(1, I):
            dp[i][0] += dp[i-1][0] + cnt[i][ord(target[0]) - ord('a')]

        for i in range(1, I):
            for j in range(1, J):
                cidx = ord(target[j]) - ord('a')
                dp[i][j] = ((dp[i-1][j-1]*cnt[i][cidx])%mod + dp[i-1][j])%mod
        return dp[-1][-1]

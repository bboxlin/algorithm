class Solution:
    """
dp[i][j] means the count of schemes with i profit and j members.
The dp equation is simple here:
dp[i + p][j + g] += dp[i][j]) if i + p < P
dp[P][j + g] += dp[i][j]) if i + p >= P
    """
    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)
class Solution:
    def maxValueOfCoins(self, A: List[List[int]], k: int) -> int:
        n = len(A)
        dp = [ [0]*(k+1) for _ in range(n) ]
        presum = [0] * n 
        for i in range(n):
            cursum = 0
            presum[i] = [cursum]
            for j in range(len(A[i])):
                cursum += A[i][j]
                presum[i].append(cursum)
 
 
        for i in range(n):
            for j in range(k+1):
                # suppose at current pile we pick x coins
                maxpick = min(j, len(A[i])) + 1
                for x in range(maxpick):
                    if i == 0:
                        dp[i][j] = presum[i][x]
                    else:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-x] + presum[i][x])
        return dp[n-1][k]
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def dfs(n, target):
            if n == 0 and target == 0:
                return 1
            if n < 0 or target < 0:
                return 0
            
            ways = 0
            for amount in range(1, k+1):
                ways += dfs(n-1, target-amount)
            return ways
        
        return dfs(n, target) % (10**9+7)
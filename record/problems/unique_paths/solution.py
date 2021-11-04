class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(m, n):
            res = 0
            if (m,n) in memo:
                return memo[(m,n)]
            if m <= 1 and n <= 1:
                return 1
            if m < 1 or n < 1:
                return 0
            res += dfs(m-1,n)
            memo[(m,n)] = res
            res += dfs(m,n-1)
            memo[(m,n)] = res
            return memo[(m,n)]
        return dfs(m,n)
            
        
        
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:    
        @cache
        def dfs(i, j, move):
            if move > maxMove:
                return 0
            if i >= m or j >= n or i < 0 or j < 0:
                return 1
            a = dfs(i+1, j, move+1) 
            b = dfs(i-1, j, move+1)
            c = dfs(i, j+1, move+1)
            d = dfs(i, j-1, move+1)
            return (a+b+c+d) % (10**9+7)
        return dfs(startRow, startColumn, 0)

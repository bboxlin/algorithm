class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            res = 1
            for di, dj in [(1,0), (0,1), (0,-1), (-1,0)]:
                if 0 <= i + di < rows and 0 <= j + dj < cols and grid[i+di][j+dj] > grid[i][j]:
                    res += dfs(i+di, j+dj) % mod 
            return res

        mod = 10**9 + 7
        total = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                total += dfs(i,j)
        return total % mod
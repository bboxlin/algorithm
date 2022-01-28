class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= R or j >= C or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            down = dfs(i+1, j)
            up = dfs(i-1, j)
            right = dfs(i, j+1)
            left = dfs(i, j-1)

            
            return down+up+right+left+1
        
        area = 0
        for i in range(R):
            for j in range(C):
                area = max(dfs(i,j),area)
        
        return area
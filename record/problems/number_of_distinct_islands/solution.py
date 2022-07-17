class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] != 1:
                return ""
            grid[r][c] = 0
            left = "l" + dfs(r, c-1)  
            right = "r" +  dfs(r, c+1) 
            down = "d" + dfs(r+1, c) 
            up = "u" + dfs(r-1, c) 
            return left+right+down+up
            
    
        ans_set = set()
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    path = dfs(i, j)
                    ans_set.add(path)
          
        return len(ans_set)
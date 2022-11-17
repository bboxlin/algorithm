class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
         
        def markIsland(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if grid[i][j] != '1':
                return 
            grid[i][j] = '0'
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                markIsland(i+di, j+dj)
        
        cnt = 0 
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    markIsland(i,j)
                    cnt += 1
                    
        return cnt
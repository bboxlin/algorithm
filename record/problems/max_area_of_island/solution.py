class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def getArea(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            if grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            area = 0
            for di,dj in [(1,0),(-1,0), (0,1), (0,-1)]:
                area += getArea(i+di, j+dj)
                
            return area + 1
        
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans, getArea(i,j))
        return ans
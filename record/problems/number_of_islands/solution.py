class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # dfs
        def markIsland(r, c):
            if r < 0 or r >= rows or c >= cols or c < 0 or grid[r][c] != '1':
                return 
            grid[r][c] = '0'
            markIsland(r+1, c)
            markIsland(r-1, c)
            markIsland(r, c+1)
            markIsland(r, c-1)

        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    markIsland(i,j)
                    ans += 1
        return ans
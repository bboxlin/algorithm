class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def isClosed(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False 
            # if reach to water
            if grid[i][j] != 0:
                return True 
            # mark visited
            grid[i][j] = 2
            f = True
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                f = f & isClosed(i+di, j+dj)
            return f

        cnt = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                # only not visited and is island we dfs
                if grid[i][j] == 0 and isClosed(i,j): 
                    cnt += 1
        return cnt
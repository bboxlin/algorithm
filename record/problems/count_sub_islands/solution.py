class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return True
            if grid2[i][j] != 1:
                return True
            
            # in a case that grid2[i][j] == 1
            # we check if grid1 is 1 or not 
            if grid1[i][j] != 1:
                return False 
            
            grid2[i][j] = 2
            issub = True
            for di, dj in [(1,0),(-1,0), (0,1), (0,-1)]:
                issub &= dfs(i+di, j+dj)
            return issub
        
        
        ans = 0
        rows = len(grid2)
        cols = len(grid2[0])
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 1 and dfs(i,j):
                    ans += 1
        return ans
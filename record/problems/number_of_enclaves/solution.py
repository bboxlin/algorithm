class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
#         def dfs(i,j):
#             if i < 0 or i >= rows or j < 0 or j >= cols:
#                 return (False, 0) 
#             if grid[i][j] != 1:
#                 return (True, 0)
#             grid[i][j] = 2
#             downok, downcnt = dfs(i+1, j)
#             upok, upcnt = dfs(i-1, j)
#             rightok, rightcnt = dfs(i, j+1)
#             leftok, leftcnt = dfs(i, j-1)
#             return (downok & upok & rightok & leftok, downcnt+upcnt+rightcnt+leftcnt+1)

#         ans = 0
#         rows = len(grid)
#         cols = len(grid[0])
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == 1:
#                     isclosed, walks = dfs(i,j)
#                     if isclosed:
#                         ans += walks
#         return ans
    
        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return (False, 0) 
            if grid[i][j] != 1:
                return (True, 0)
            grid[i][j] = 2
            ok,cnt = True,0
            for di, dj in [(1,0),(-1,0), (0,1),(0,-1)]:
                isok, cntnum = dfs(i+di, j+dj)
                ok &= isok
                cnt += cntnum
            return (ok, cnt+1)
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    isclosed, walks = dfs(i,j)
                    if isclosed:
                        ans += walks
        return ans
    
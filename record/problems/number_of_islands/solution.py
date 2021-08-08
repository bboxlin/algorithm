class Solution:

    def numIslands(self, grid: List[List[str]]) -> int: 
        islands = 0
        row, col = len(grid), len(grid[0])
        def bfs(r,c):
            que = collections.deque()
            que.append((r,c))
            grid[r][c] = '0'
            while que:
                i, j = que.popleft()
                dir = ((i-1,j),(i+1,j),(i,j+1),(i,j-1))
                for di,dj in dir:
                    if di in range(row) and dj in range(col) and grid[di][dj] == '1':
                        grid[di][dj] = '0'
                        que.append((di,dj))
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(i,j)
                    islands += 1 
        return islands
    
#     def numIslands(self, grid: List[List[str]]) -> int: 
#         islands = 0
#         row, col = len(grid), len(grid[0])
#         visit = set()
#         def bfs(r,c):
#             que = collections.deque()
#             que.append((r,c))
#             visit.add((r,c))
#             while que:
#                 i, j = que.popleft()
#                 dir = ((i-1,j),(i+1,j),(i,j+1),(i,j-1))
#                 for di,dj in dir:
#                     if di in range(row) and dj in range(col) and grid[di][dj] == '1' and (di,dj) not in visit:
#                         visit.add((di,dj))
#                         que.append((di,dj))
        
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == '1' and (i,j) not in visit:
#                     bfs(i,j)
#                     islands += 1 
#         return islands
        
        
    #dfs    
#     def numIslands(self, grid: List[List[str]]) -> int:
          
#         islands = 0
#         row, col = len(grid), len(grid[0])
        
#         def dfs(r,c):
#             if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
#                 return 0
#             grid[r][c] = '0'
#             dfs(r-1,c)
#             dfs(r+1,c)
#             dfs(r,c+1)
#             dfs(r,c-1)
#             return 1 
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == '1':
#                     islands = islands + dfs(i,j)    
        
#         return islands
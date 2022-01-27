class Solution:
    
    # -------------------
    # BFS
    # -------------------
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
#         color = image[sr][sc]
#         if color == newColor: return image
        
#         R, C = len(image), len(image[0])
#         q = collections.deque([(sr,sc)])
        
#         while q:
#             level_size = len(q)
#             for _ in range(level_size):
#                 i, j = q.popleft()
#                 image[i][j] = newColor
#                 for d in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
#                     di, dj = d
#                     ni, nj = i + di, j + dj
#                     if ni >= 0 and nj >= 0 and ni < R and nj < C and image[ni][nj] == color:
#                         q.append((ni,nj))
#         return image

    # -------------------
    # DFS
    # -------------------
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        #if color == newColor: return image
        def dfs(i, j):
            if i < 0 or j < 0 or i >= R or j >= C or image[i][j] != color or image[i][j] == newColor:
                return 
            image[i][j] = newColor
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        dfs(sr, sc)
        return image
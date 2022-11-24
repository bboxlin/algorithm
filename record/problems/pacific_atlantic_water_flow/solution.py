class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(i,j, ph, container):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 
            if (i,j) in container:
                return 
            if heights[i][j] < ph:
                return 
            container.add((i,j))
            for di, dj in [(1,0),(-1,0), (0,1), (0,-1)]:
                dfs(i+di, j+dj, heights[i][j],container)
     
        pacific = set() 
        for j in range(cols):
            dfs(0,j,heights[0][j], pacific)
        for i in range(rows):
            dfs(i,0,heights[i][0], pacific)
        
        atlantic = set()
        for j in range(cols):
            dfs(rows-1, j, heights[rows-1][j], atlantic)
        for i in range(rows):
            dfs(i,cols-1,heights[i][cols-1], atlantic)
        
        ans = pacific & atlantic
        return [ [i,j] for i, j in ans]
        
        
        
        
    """
    1,2
    4,3
    """
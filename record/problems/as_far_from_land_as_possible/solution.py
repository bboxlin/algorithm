class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Basically, land expansion 
        BFS each step is a step of BFS
        """
        q = deque([])
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i,j))
        
        ans = -1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft() 
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if 0 <= i + di < rows and 0 <= j + dj < cols and grid[i+di][j+dj] == 0:
                        grid[i+di][j+dj] = 1
                        q.append((i+di, j+dj))
            ans += 1 
             
                        
        return ans if ans != 0 else -1
                        
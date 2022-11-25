class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if grid[0][0] != 0:
            return -1 
        
        q = deque([ (0,0) ])
        ans = 1
        grid[0][0] = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == rows - 1 and j == cols - 1:
                    return ans 
                 
                for di, dj in [(1,0),(-1,0),(0,1),(0,-1), (1,-1), (-1,1), (1,1), (-1,-1)]:
                    if 0 <= i + di < rows and 0 <= j + dj < cols and grid[i+di][j+dj] == 0:
                        # we want to mark visited here immediately 
                        grid[i+di][j+dj] = 1
                        q.append((i+di,j+dj))
            ans += 1
        return -1

    """
    1 0 0 
    1 1 0 
    1 1 0 
    """
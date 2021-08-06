class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        rotten = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.append((i,j,0))
                if grid[i][j] == 1:
                    fresh += 1
        min = 0
        while rotten:
            i,j,min = rotten.popleft()
            for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1
                    rotten.append((r,c,min+1))
        if fresh > 0: return -1
        else: return min

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        pos = [(0,0), (0,1), (0,2), (1, 1), (2, 1), (2,0), (2,2)]
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if i + 2 < rows and j + 2 < cols:
                    cursum = 0
                    for di, dj in pos:
                        newi = i + di
                        newj = j + dj 
                        cursum += grid[newi][newj]
                    ans = max(cursum, ans)
        return ans
                  
                        
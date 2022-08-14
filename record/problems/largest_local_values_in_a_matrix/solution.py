class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
         
        n, m = len(grid), len(grid[0])
        ans = [ [0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(m-2):
                for ii in range(i, i+3):
                    for jj in range(j, j+3):
                        ans[i][j] = max(ans[i][j], grid[ii][jj])
        return ans
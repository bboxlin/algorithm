class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dp = [ [math.inf] *cols for _ in range(rows) ]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    up = dp[i-1][j] if i > 0 else math.inf 
                    left = dp[i][j-1] if j > 0 else math.inf 
                    dp[i][j] = min(up,left) + 1
        
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    down = dp[i+1][j] if i < rows-1 else math.inf 
                    right = dp[i][j+1] if j < cols - 1 else math.inf 
                    dp[i][j] = min( min(down, right) + 1, dp[i][j] ) 
        return dp
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(1, rows):
            for j in range(cols):
                up = matrix[i-1][j]
                upleft = matrix[i-1][j-1] if j > 0 else math.inf
                upright = matrix[i-1][j+1] if j+1 < cols else math.inf 
                matrix[i][j] += min(up, upleft, upright)
        return min(matrix[-1])
 
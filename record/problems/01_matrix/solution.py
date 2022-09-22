class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] + 1 if r > 0 else math.inf
                    left = mat[r][c - 1] + 1 if c > 0 else math.inf
                    mat[r][c] = min(top, left) # very important as we will lookback mat we keep the cur min

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] + 1 if r < m - 1 else math.inf
                    right = mat[r][c + 1] + 1 if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom, right) # very important as we will lookback mat we keep the cur min

        return mat
                    
        
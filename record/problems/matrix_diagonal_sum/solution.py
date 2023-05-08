class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(n):
            if (i,i) != (i, n-i-1):
                res += mat[i][i]
                res += mat[i][n-i-1]
            else:
                res += mat[i][i]
        return res
        
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        if R == r and C == c or r*c != R*C:
            return mat 
        ans = [[0]*c for _ in range(r)]
        for i in range(R*C):
            ans[i//c][i%c] = mat[i//C][i%C]
             
        return ans
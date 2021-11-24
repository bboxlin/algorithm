class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i > 0 and j > 0 and matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        for j in range(cols):
            col = []
            for i in range(rows):
                col.append(matrix[i][j])
            ans.append(col)
        return ans
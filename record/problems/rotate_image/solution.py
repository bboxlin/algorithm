class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, t = 0,0
        r, d = len(matrix)-1, len(matrix)-1
        while l < r:
            for i in range(r-l):
                temp = matrix[t][l+i]
                matrix[t][l+i] = matrix[d-i][l]
                matrix[d-i][l] = matrix[d][r-i]
                matrix[d][r-i] = matrix[t+i][r]
                matrix[t+i][r] = temp
            l+=1
            r-=1
            t+=1
            d-=1
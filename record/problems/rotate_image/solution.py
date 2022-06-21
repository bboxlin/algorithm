class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = top = 0
        right = bottom = len(matrix)-1
        while left < right:
            steps = right - left
            for i in range(steps):
                tem = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top + i][right]
                matrix[top + i][right] = tem
            left += 1
            right -=1 
            top += 1
            bottom -= 1
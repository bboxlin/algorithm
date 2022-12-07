class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = top = 0
        right = bottom = len(matrix)-1
        while left < right:
            steps = right - left
            for i in range(steps):
                temp = matrix[top][left+i]
                # top to right = left bottom to up
                matrix[top][left+i] = matrix[bottom-i][left]
                # left bottom to up = bottom to left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # bottom to left = right top to down
                matrix[bottom][right-i] = matrix[top+i][right]
                # right top to down = top to right
                matrix[top+i][right] = temp
            left += 1
            right -= 1
            bottom -= 1
            top += 1


        
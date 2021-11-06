class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW, COL = len(matrix), len(matrix[0])
        
        row_w_zero, col_w_zero = False, False
        
        for j in range(COL):
            if matrix[0][j] == 0:
                row_w_zero = True
        
        for i in range(ROW):
            if matrix[i][0] == 0:
                col_w_zero = True
        
        
        # loop through and mark 0s on first row and first col
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # inner shell set to 0
        for i in range(1, ROW):
            for j in range(1, COL):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if row_w_zero:
            for j in range(COL):
                matrix[0][j] = 0
        
        if col_w_zero:
            for i in range(ROW):
                matrix[i][0] = 0
        
            
                
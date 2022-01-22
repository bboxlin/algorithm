class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        res = []
        ROW, COL = len(matrix), len(matrix[0])
        direc = {0:[0,1], 1:[1,0], 2:[0, -1], 3:[-1, 0]}
        d = 0
        r, c, dr, dc = 0, 0, 0, 1
        for _ in range(ROW*COL):
            res.append(matrix[r][c])
            matrix[r][c] = 888
            # check for the next position, if in valid, adjust dr and dc
            if r+dr >= ROW or c+dc >= COL or matrix[r+dr][c+dc] == 888:
                d = (d+1)%4
                dr, dc = direc[d]
            r += dr 
            c += dc
        return res
                
            
            
                
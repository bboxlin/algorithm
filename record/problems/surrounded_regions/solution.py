class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def markUnsurrounded(i, j):
            if i < 0 or i >= R or j < 0 or j >= C or board[i][j] != 'O': 
                return 
            board[i][j] = '*'
            markUnsurrounded(i+1, j)
            markUnsurrounded(i, j+1)
            markUnsurrounded(i-1, j)
            markUnsurrounded(i, j-1)
            
        R, C = len(board), len(board[0])
        for r in range(R):
            if board[r][0] == 'O': markUnsurrounded(r, 0)
            if board[r][C-1] == 'O': markUnsurrounded(r, C-1)
        
        for c in range(C):
            if board[0][c] == 'O': markUnsurrounded(0, c)
            if board[R-1][c] == 'O': markUnsurrounded(R-1, c)
        
        # flip O -> X (Surrounded!)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O': board[r][c] = 'X'
                elif board[r][c] == '*': board[r][c] = 'O'
        
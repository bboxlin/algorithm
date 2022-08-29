class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        def countSurr(i, j):
            numAlive = 0
            for di, dj in [(1,0), (-1,0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1,1)]:
                if 0 <= i + di < self.n and 0 <= j+dj < self.m: 
                    numAlive += (refBoard[i+di][j+dj] == 1)
            return numAlive
        
        refBoard = deepcopy(board)
        self.n = len(board)
        self.m = len(board[0])
        for i in range(self.n):
            for j in range(self.m):
                numAlive = countSurr(i,j)
                if refBoard[i][j] == 1 and numAlive < 2 or numAlive >3:
                    board[i][j] = 0
                if refBoard[i][j] == 0 and numAlive == 3:
                    board[i][j] = 1

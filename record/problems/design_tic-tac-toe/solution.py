class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagLeft = 0
        self.diagRight = 0

    def move(self, row: int, col: int, player: int) -> int:
        amount = 1 if player == 1 else -1
        self.rows[row] += amount
        self.cols[col] += amount
        if row == col: self.diagLeft += amount 
        if row+col == self.n - 1: self.diagRight += amount 
        print(self.diagLeft, self.n)
        #check 
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagLeft) == self.n or abs(self.diagRight) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
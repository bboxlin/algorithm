class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X':
                    if board[i][j] == '.': continue 
                    if i > 0 and board[i-1][j] == 'X': continue 
                    if j > 0 and board[i][j-1] == 'X': continue
                    ans += 1
                         
        return ans 
                
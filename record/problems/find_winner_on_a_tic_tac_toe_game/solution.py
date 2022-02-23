class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = 3
        row = [0]*N
        col = [0]*N
        left_diag = 0 
        right_diag = 0
        
        # suppose A = 1, B = -1
        player = 1
        for i, j in moves:
            
            # left diag
            if i == j:
                left_diag += player
            
            # right diag
            if (i+j) == N-1:
                right_diag += player
                
            row[i] += player
            col[j] += player
            
            
            if abs(row[i]) == N or abs(col[j]) == N or abs(left_diag) == N or abs(right_diag) == N:
                if player == 1: return 'A'
                else: return 'B'
 
            
            player *= -1
        
        if len(moves) < N*N:
            return "Pending"
        
        return "Draw"
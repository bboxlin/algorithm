class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, k):
            if k == len(word):
                return True 
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False 
            if board[i][j] != word[k]:
                return False 

            val = board[i][j]
            board[i][j] = '#'
            exists = False 
            for di, dj in [(1, 0), (-1, 0), (0,-1), (0,1)]:
                exists |= dfs(i+di, j+dj, k+1)
            board[i][j] = val
 
            return exists
            
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True 
        return False 
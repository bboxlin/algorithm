class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, k, curval=None):
            if k == len(word): return True
            if i < 0 or j < 0 or i >= R or j >= C or board[i][j] != word[k]: return False
            
            # curval recorded, mark this position # meaning visited
            curval, board[i][j] = board[i][j], '#'
            res = dfs(i+1, j, k+1, curval) or dfs(i-1, j, k+1, curval) or dfs(i, j+1, k+1, curval) or dfs(i, j-1, k+1, curval)
            
            # when backtrack reverse the visited to its original value
            board[i][j] = curval
            return res
        
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):return True
        return False
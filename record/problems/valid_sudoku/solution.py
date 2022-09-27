class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        rowset = set()
        colset = set() 
        block = defaultdict(set)
        
        for i in range(rows):
            for j in range(cols):
                rownum = board[i][j]
                colnum = board[j][i]
                
                if rownum in rowset: 
                    return False 
                if colnum in colset: 
                    return False
                
                if rownum != '.': rowset.add(rownum)
                if colnum != '.': colset.add(colnum)
                
                key = (i // 3, j //3)
                if key in block.keys() and board[i][j] in block[key]:
                    return False
                if board[i][j] != '.':
                    block[key].add(board[i][j])
            
            rowset.clear()
            colset.clear() 
        
        return True
                
                
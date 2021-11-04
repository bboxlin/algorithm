class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        block = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if board[i][j] != '.':
                    # check for row
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        return False
                    
                    # check for block
                    if board[i][j] in block[(i//3, j//3)]:
                        return False
                    else:
                        block[(i//3, j//3)].add(board[i][j])
                    
                # check for column
                if board[j][i] != '.':
                    if board[j][i] not in col:
                        col.add(board[j][i])
                    else:
                        return False
                
                
            col.clear()
            row.clear()
        return True
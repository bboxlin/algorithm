import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check for rows 
        rowset, colset = set(), set()
        
        # check for box
        boxTable = collections.defaultdict(set)
                
        for row in range(len(board)):
            for col in range(len(board[row])):
                rowNum = board[row][col]
                colNum = board[col][row]
                boxkey = (row//3, col//3)
                if boxkey in boxTable.keys() and rowNum in boxTable[boxkey]:
                    return False
                if rowNum in rowset:
                    return False
                if colNum in colset:
                    return False
                if rowNum != '.':
                    rowset.add(rowNum)
                    boxTable[boxkey].add(rowNum)
                if colNum != '.':
                    colset.add(colNum)  
            rowset.clear()
            colset.clear()
        return True
        
        
        
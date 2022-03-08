# 1
# 1 1 
# 1 2 1 
# 1 3 3 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for r in range(1, numRows):
            prevRow = res[-1]
            row = [1]
            for c in range(1, len(res[-1])):
                row.append(prevRow[c-1] + prevRow[c])
            row.append(1)
            res.append(row)
        return res
                
            
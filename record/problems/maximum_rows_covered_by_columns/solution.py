class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        C = len(mat[0])
        columns = [c for c in range(C)]
        coms = list(combinations(columns, cols))
        
        ans = 0
        for com in coms:
            com = set(com)
            curComCnt = 0
            for rowSublist in mat:
                isCovered = True
                for c in range( len(rowSublist) ):
                    if rowSublist[c] == 1 and c not in com:
                        isCovered = False
                        break 
                if isCovered:
                    curComCnt += 1
            ans = max(ans, curComCnt)
        return ans
                
       
            
        
        
              
                    
                
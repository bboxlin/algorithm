class Solution:
    '''
          a  when encounter a'next is * two path to choose
        /   \
(i+1, j)    (i, j+2)
    
    '''
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs (i,j):
            if i >= len(s) and j >= len(p): return True
            if j >= len(p): return False
            flag = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j+1) < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or (flag and dfs(i+1,j))
            if flag: return dfs(i+1, j+1)
            return False
        return dfs(0,0)
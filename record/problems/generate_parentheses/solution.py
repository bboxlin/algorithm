class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, lcnt, rcnt):
            if lcnt == n and rcnt == n:
                res.append(s)
                return 
            if lcnt < n:
                dfs(s+'(', lcnt+1, rcnt)
            if rcnt < lcnt:
                dfs(s+')', lcnt, rcnt+1)
        dfs('', 0, 0)
        return res
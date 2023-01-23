class Solution:
    def confusingNumberII(self, n: int) -> int: 
        def backtrack(cur, rotate):
            if cur and int(cur) > n:
                return    
            nonlocal res 
            if cur != rotate:
                res += 1
            for c in con:
                if c == '0' and len(cur) == 0: continue
                backtrack(cur+c, mp[c] + rotate)
        res = 0
        con = ['0','1','6', '8', '9']
        mp = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        backtrack("", "")
        return res
    
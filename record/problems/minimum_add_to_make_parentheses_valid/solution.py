class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        leftp = 0
        res = 0
        for c in s:
            if c == '(':
                leftp += 1
            elif c == ')':
                if leftp <= 0:
                    res += 1
                else:
                    leftp -= 1
        
        res += leftp
        
        return res
                
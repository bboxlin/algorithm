class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lens, lent = len(s), len(t)
        if lens != lent: return False 
        
        s2t, t2s = {}, {}
        for i in range(lens):
            si, ti = s[i], t[i]
            if si in s2t.keys() and s2t[si] != ti:
                return False 
            if ti in t2s.keys() and t2s[ti] != si:
                return False 
            s2t[si] = ti
            t2s[ti] = si
            
        return True
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        res = ""
        for c in order:
            if c in freq:
                res += freq[c]*c
                freq[c] = 0
        
        for k in freq.keys():
            if freq[k] > 0:
                res += k*freq[k]
    
        return res
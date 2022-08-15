class Solution:

    def romanToInt(self, s: str) -> int:
        lookup = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        n = len(s)
        for i in range(n):
            if i == n-1:
                res += lookup[s[i]]
            else:
                if lookup[s[i+1]] > lookup[s[i]]:
                    res -= lookup[s[i]]
                else:
                    res += lookup[s[i]]
                
        return res
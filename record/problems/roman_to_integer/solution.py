class Solution:
    '''
    i, i+1, i+2 ...
    in general 
    where i > i+1 > i+2 -> Roman[i i+1 i+2] --> 
    
    if i < i+1
    then i = -i 
    only a i can exsit in that way
    '''
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
        for i in range(len(s)):
            if i+1 < len(s) and lookup[s[i]] < lookup[s[i+1]]:
                res -= lookup[s[i]]
            else:
                res += lookup[s[i]]
        return res        
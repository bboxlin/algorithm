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
        for i in range(len(s)-1):
            cur = s[i]
            nex = s[i+1]
            if lookup[nex] > lookup[cur]:
                res -= lookup[cur]
            else:
                res += lookup[cur]
                
        res += lookup[s[-1]]
        return res
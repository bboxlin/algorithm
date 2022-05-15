class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexTable = {}
        i, j = 0, 0
        maxlen = 0
        while j < len(s):
            curchar = s[j]
            if curchar in indexTable:
                i = max(indexTable[curchar], i)
            maxlen = max(maxlen, j-i+1)
            indexTable[curchar] = j+1
            j += 1
        return maxlen
            
             

        
            
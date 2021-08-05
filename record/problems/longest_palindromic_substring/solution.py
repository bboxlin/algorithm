class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
        def subString(l,r):
            while(l>=0 and r<len(s) and s[l] == s[r]):
                r = r+1 
                l = l-1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            #单数情况, 中间独特
            test = subString(i,i)
            if len(test) > len(res): res=test
                
            #双数情况, 邻居相等
            test = subString(i,i+1)
            if len(test) > len(res): res=test
        
        return res
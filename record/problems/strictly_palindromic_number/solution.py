class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def convert2BaseNumStr(base, num):
            ans = ""
            while num:
                rem = num % base 
                num = num // base 
                ans = str(rem) + ans
            return ans
        
        def isPalindromic(s):
            l, r = 0, len(s) - 1 
            while l < r:
                if s[l] != s[r]: return False 
                l += 1
                r -= 1
            return True
        
        for base in range(2, n-1):
            baseStr = convert2BaseNumStr(base, n)
            if isPalindromic(baseStr) == False: 
                return False 
        return True
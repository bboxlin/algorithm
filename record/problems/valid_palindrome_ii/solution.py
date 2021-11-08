class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        
        def isPanlindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        while l < r:
            if s[l] != s[r]:
                return isPanlindrome(l+1,r) or isPanlindrome(l,r-1)
            l+=1
            r-=1
        return True



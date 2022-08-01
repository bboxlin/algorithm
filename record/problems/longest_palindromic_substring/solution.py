class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def getPan(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        n = len(s)
        ans = ""
        for i in range(n):
            p1 = getPan(i, i)
            p2 = getPan(i, i+1)
            ans = p1 if len(p1) > len(ans) else ans
            ans = p2 if len(p2) > len(ans) else ans
        return ans
            
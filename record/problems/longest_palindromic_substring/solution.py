class Solution:   
    def longestPalindrome(self, s: str) -> str:   
        def getPalindrome(l, r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l+1, r-1)
        start, end = 0, 0
        for i in range(len(s)):
            p1_start, p1_end = getPalindrome(i, i)
            p2_start, p2_end = getPalindrome(i, i+1)
            p1_len = p1_end - p1_start
            p2_len = p2_end -p2_start 
            if p1_len > end - start:
                start = p1_start
                end = p1_end
            if p2_len > end - start:
                start = p2_start
                end = p2_end
        return s[start: end+1]
                
                
                
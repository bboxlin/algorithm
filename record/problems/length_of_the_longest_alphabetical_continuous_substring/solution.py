class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0
        while l < n:
            r = l+1
            while r < n and ord(s[r]) == ord(s[r-1]) + 1:
                r += 1
            ans = max(ans, r-l)
            l = r 
            # "awy" 1
        return ans
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_freq = 0 # of consecutives 
        i, ans = 0, 0
        while i < len(s):
            cnt = 0
            c = s[i]
            while i < len(s) and s[i] == c:
                cnt += 1
                i += 1
            ans += min(cnt, prev_freq)
            prev_freq = cnt
        return ans
                
                
    
                
            
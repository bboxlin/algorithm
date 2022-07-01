import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0 
        for ch, cnt in freq.items():
            if cnt % 2 == 0:
                ans += cnt 
            else:
                ans += cnt - 1
            
            if ans % 2 == 0 and cnt % 2 == 1:
                ans += 1
        return ans
    
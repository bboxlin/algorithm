import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for c, cnt in freq.items():
            x = cnt // 2 * 2
            ans += x
            if ans % 2 == 0 and cnt % 2 == 1:
                ans += 1            
        return ans
    
    # "abccccdd"
    # a:1
    # b:1
    # d:2
    # c:4
    
    #2+2*2+1 = 7
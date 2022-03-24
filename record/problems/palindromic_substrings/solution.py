class Solution:
    def countSubstrings(self, s: str) -> int:
        def cntPalindrom(l,r):
            num = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                num += 1
            return num
        total_cnt = 0
        for i in range(len(s)):
            cnt1 = cntPalindrom(i, i)
            cnt2 = cntPalindrom(i, i+1)
            total_cnt += cnt1 + cnt2
        return total_cnt
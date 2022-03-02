class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L, R = len(s), len(t)
        l, r = 0, 0
        while l < L and r < R:
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
        return l == L
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1cnt = [0] * 26
        s2cnt = [0] * 26
        for c in s1:
            s1cnt[ord(c)-ord('a')] += 1
        for c in s2:
            s2cnt[ord(c)-ord('a')] += 1
        if s1cnt != s2cnt: 
            return False
        mis = 0
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                mis += 1
        return mis <= 2
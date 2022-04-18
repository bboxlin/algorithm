class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freq = Counter(s)
        for c in t:
            if c not in freq:
                return False
            freq[c] -= 1
            if freq[c] < 0: return False
        return True
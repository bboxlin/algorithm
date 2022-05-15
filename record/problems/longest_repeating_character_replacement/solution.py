import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqTable = collections.defaultdict(int)
        l, maxlen = 0, 0
        for r in range(len(s)):
            freqTable[s[r]] += 1
            while (r - l + 1) - max(freqTable.values()) > k:
                freqTable[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
            
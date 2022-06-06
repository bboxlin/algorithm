import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        dic = collections.Counter(s)
        freqVisited = set()
        res = 0
        for c in set(s):
            freq = dic[c]
            while freq in freqVisited:
                freq -= 1
                res += 1
            if freq > 0:
                freqVisited.add(freq)
        return res
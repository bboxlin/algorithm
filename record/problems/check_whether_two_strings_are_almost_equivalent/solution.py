class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        wcnt1 = Counter(word1)
        wcnt2 = Counter(word2)
        n = len(word1)
        for i in range(n):
            w1 = word1[i]
            w2 = word2[i]
            if abs(wcnt1[w1] - wcnt2[w1]) > 3:
                return False 
            if abs(wcnt1[w2] - wcnt2[w2]) > 3:
                return False 
        return True
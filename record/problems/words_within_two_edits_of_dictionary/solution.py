class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def isWithinTwoEdits(x, y):
            n = len(x)
            diff = 0
            for i in range(n):
                if x[i] != y[i]:
                    diff += 1
            return diff <= 2
        
        res = []
        for w1 in queries:
            for w2 in dictionary:
                if isWithinTwoEdits(w1, w2):
                    res.append(w1)
                    break
        return res

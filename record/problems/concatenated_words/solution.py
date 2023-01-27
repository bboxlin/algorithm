class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        @cache
        def canMatch(word):
            for i in range(len(word)):
                p = word[:i]
                q = word[i:]
                if p in wordset and q in wordset:
                    return True
                if p in wordset and canMatch(q):
                    return True 
                if q in wordset and canMatch(p):
                    return True
            return False

        res = []
        wordset = set(words)
        for word in words:
            if canMatch(word):
                res.append(word)
        return res

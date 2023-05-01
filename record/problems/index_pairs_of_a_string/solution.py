class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        wordset = set(words)
        n = len(text)
        for i in range(n):
            for j in range(i+1, n+1):
                word = text[i:j]
                if word in wordset:
                    res.append([i,j-1])
        return res
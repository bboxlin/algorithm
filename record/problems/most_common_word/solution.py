class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbol = "!?',;."
        for c in symbol:
            paragraph = paragraph.replace(c, " ")

        paragraphlst = paragraph.lower().split()
        memo = {}

        for word in paragraphlst:
            if word in memo:
                memo[word] += 1
            else:
                memo[word] = 1

        banSet = set(banned)
        maxCount = 0
        res = ""
        for word in memo:
            if memo[word] > maxCount and word not in banSet:
                res = word
                maxCount = memo[word]
        return res

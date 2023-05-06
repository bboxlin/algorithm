class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aeiou'
        n = len(s)

        res = 0
        for i in range(k):
            if s[i] in vowel:
                res += 1
        
        curmax = res
        for i in range(k, n):
            if s[i] in vowel:
                curmax += 1
            if s[i-k] in vowel:
                curmax -= 1
            res = max(res, curmax)
        return res


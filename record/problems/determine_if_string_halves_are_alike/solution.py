class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        m = n // 2 
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        cnter1 = 0
        cnter2 = 0
        for i in range(m):
            if s[i] in vowels:
                cnter1 += 1
        for i in range(m, n):
            if s[i] in vowels:
                cnter2 += 1
        return cnter1 == cnter2
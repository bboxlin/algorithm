class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
        leftone = [0]*n
        rightzero = [0]*n

        for i in range(1, n):
            leftone[i] = leftone[i-1] + (1 if s[i-1] == '1' else 0)
        for i in range(n-2, -1, -1):
            rightzero[i] = rightzero[i+1] + (1 if s[i+1] =='0' else 0)
        
        minflip = n
        for i in range(n):
            minflip = min(minflip, leftone[i] + rightzero[i])
        return minflip

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        preB, posA = [0]*n, [0]*n
        for i in range(n):
            if i == 0:
                preB[i] = 1 if s[i] == 'b' else 0
            else:
                preB[i] = preB[i-1] + (1 if s[i] == 'b' else 0) 
                
        for i in range(n-1, -1, -1):
            if i == n-1:
                posA[i] = 1 if s[i] == 'a' else 0
            else:
                posA[i] = posA[i+1] + (1 if s[i] == 'a' else 0) 
        
        min_del = n
        for i in range(n):
            min_del = min(preB[i] + posA[i] - 1 , min_del)
        return min_del
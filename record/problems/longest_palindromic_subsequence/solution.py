class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        def helper(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i > j:
                
                return 0
            if i == j:
            
                return 1
            
            if s[i] == s[j]:
                memo[(i,j)] = 2 + helper(i+1, j-1)
                return memo[(i,j)] 
            else:
                memo[(i,j)] = max(helper(i+1, j), helper(i, j-1))
                return memo[(i,j)] 
        
        return helper(0, len(s)-1)
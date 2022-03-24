class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        cache = {}
        def helper(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(text1) or j >= len(text2):
                cache[(i,j)] = 0
                return 0
            elif text1[i] == text2[j]:
                cache[(i,j)] = 1 + helper(i+1, j+1)
                return cache[(i,j)]
            else:
                cache[(i,j)] = max(helper(i+1, j), helper(i, j+1))
                return cache[(i,j)]
        return helper(0, 0)
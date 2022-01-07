class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = collections.defaultdict(int)
        i = 0
        res = 0
        for j, c in enumerate(s):
            if c in memo.keys():
                i = max(memo[c] + 1, i)
            memo[c] = j
            res = max(res, j-i+1)
        return res
        

        
            